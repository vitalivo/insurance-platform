
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Типы данных
export interface Product {
  id: number;
  name: string;
  display_name: string;
  description: string;
  is_active: boolean;
  fields?: ProductField[];
}

export interface ProductField {
  id: number;
  field_name: string;
  field_type: string;
  is_required: boolean;
  choices: any;
  order: number;
}

export interface ApplicationData {
  product: number;
  full_name: string;
  phone: string;
  email: string;
  birth_date: string;
  personal_data_consent: boolean;
  comment?: string;
  additional_data?: any;
}

// API функции
export const productsAPI = {
  getAll: () => apiClient.get<{results: Product[]}>('/products/'),
  getByName: (name: string) => apiClient.get<Product>(`/products/${name}/`),
};

export const applicationsAPI = {
  create: (data: ApplicationData) => apiClient.post('/applications/create/', data),
  getByNumber: (number: string) => apiClient.get(`/applications/${number}/`),
};
