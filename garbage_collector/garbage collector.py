import gc


class SampleClass:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} oluşturuldu')


for i in range(10):
    obj = SampleClass(f'Nesne-{i}')


gc.collect()


print("Toplam Nesne Sayısı:", len(gc.get_objects()))
