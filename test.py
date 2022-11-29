
from whylogs.core import DatasetProfile, DatasetProfileView
import pandas as pd

df = pd.read_csv('./data.csv')

profile1 = DatasetProfile()
profile1.track(df)

ser = profile1.view().serialize()
view = DatasetProfileView.deserialize(ser)

profile2 = DatasetProfile()
profile2.track(df)
view.merge(profile2.view()) # error
