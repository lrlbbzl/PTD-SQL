from transformers import AutoTokenizer, AutoModel, AutoConfig
from torch.utils.data.dataset import Dataset
import torch
import csv
import json
from torch import nn
from abc import ABC
from typing import List

class TextDataset(Dataset):
    def __init__(self, args, type):
        if type == 'train':
            self.data_path = args.train_data
        elif type == 'test':
            self.data_path = args.test_data
        self.tokenizer = AutoTokenizer.from_pretrained(args.plm_path)
        x = json.load(open(self.data_path, 'r'))
        self.data = [xx['question'] for xx in x]        
    
    def __len__(self, ):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.data[idx]
        input_tokens = self.tokenizer(text, max_length=128, 
                                    truncation=True, add_special_tokens=True)
        return {
            'input_ids': input_tokens['input_ids'],
            'token_type_ids': input_tokens['token_type_ids'],
            'attention_mask': input_tokens['attention_mask'],
        }
    

class CustomBertModel(nn.Module, ABC):
    def __init__(self, args):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(args.plm_path)
        self.tokenizer = AutoTokenizer.from_pretrained(args.plm_path)

    def forward(self, input_ids, attention_mask, token_type_ids):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        last_hidden_state = outputs.last_hidden_state
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(last_hidden_state.size()).float()
        sum_embeddings = torch.sum(last_hidden_state * input_mask_expanded, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-4)
        output_vector = sum_embeddings / sum_mask
        return output_vector
    
    def collate(self, batch_data: List[dict]) -> dict:

        tail_token_ids, tail_mask = self.to_indices_and_mask(
            [torch.LongTensor(ex['input_ids']) for ex in batch_data],
            pad_token_id=self.tokenizer.pad_token_id)
        tail_token_type_ids = self.to_indices_and_mask(
            [torch.LongTensor(ex['token_type_ids']) for ex in batch_data],
            need_mask=False)
        
        batch_dict = {
            'input_ids': tail_token_ids,
            'attention_mask': tail_mask,
            'token_type_ids': tail_token_type_ids,
        }

        return batch_dict

    def to_indices_and_mask(self, batch_tensor, pad_token_id=0, need_mask=True):
        mx_len = max([t.size(0) for t in batch_tensor])
        batch_size = len(batch_tensor)
        indices = torch.LongTensor(batch_size, mx_len).fill_(pad_token_id)
        # For BERT, mask value of 1 corresponds to a valid position
        if need_mask:
            mask = torch.ByteTensor(batch_size, mx_len).fill_(0)
        for i, t in enumerate(batch_tensor):
            indices[i, :len(t)].copy_(t)
            if need_mask:
                mask[i, :len(t)].fill_(1)
        if need_mask:
            return indices, mask
        else:
            return indices