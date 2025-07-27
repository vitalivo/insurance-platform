
// Mock данные для демо версии
export const mockProducts = {
  osago: {
    id: 1,
    name: 'osago',
    display_name: 'ОСАГО',
    description: 'Обязательное страхование автогражданской ответственности'
  },
  kasko: {
    id: 2,
    name: 'kasko',
    display_name: 'КАСКО',
    description: 'Добровольное страхование транспортных средств'
  },
  ifl: {
    id: 3,
    name: 'ifl',
    display_name: 'Страхование жизни',
    description: 'Индивидуальное страхование жизни'
  },
  ns: {
    id: 4,
    name: 'ns',
    display_name: 'Накопительное страхование',
    description: 'Накопительное страхование жизни'
  },
  mortgage: {
    id: 5,
    name: 'mortgage',
    display_name: 'Ипотечное страхование',
    description: 'Страхование при ипотечном кредитовании'
  },
  klezh: {
    id: 6,
    name: 'klezh',
    display_name: 'Страхование недвижимости',
    description: 'Комплексное страхование недвижимости'
  }
};

export const mockAPI = {
  getProduct: async (name: string) => {
    await new Promise(resolve => setTimeout(resolve, 500)); // Имитация задержки
    const product = mockProducts[name as keyof typeof mockProducts];
    if (!product) throw new Error('Product not found');
    return { data: product };
  },
  
  createApplication: async (data: any) => {
    await new Promise(resolve => setTimeout(resolve, 1000)); // Имитация задержки
    const appNumber = `DEMO-${Date.now()}`;
    return { 
      data: { 
        application_number: appNumber,
        status: 'pending'
      } 
    };
  },
  
  trackApplication: async (number: string) => {
    await new Promise(resolve => setTimeout(resolve, 500));
    return {
      data: {
        application_number: number,
        status: 'pending',
        created_at: new Date().toISOString(),
        product_name: 'ОСАГО'
      }
    };
  }
};
