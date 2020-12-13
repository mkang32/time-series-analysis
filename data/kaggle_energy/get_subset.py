df_train = pd.read_csv('train.csv')
df_train_w = pd.read_csv('weather_train.csv')
df_test = pd.read_csv('test.csv')
df_test_w = pd.read_csv('weather_test.csv')

building_id = 1249
site_id = 14

df_train_sub = df_train[(df_train['building_id']==building_id) & (df_train['meter']==1)]
df_test_sub = df_test[(df_test['building_id']==building_id) & (df_test['meter']==1)]
df_train_w_sub = df_train_w[df_train_w['site_id']==site_id]
df_test_w_sub = df_test[df_test['building_id']==site_id]

df_train_sub.to_csv('train_bid_1249.csv', index=False)
df_test_sub.to_csv('test_bid_1249.csv', index=False)
df_train_w_sub.to_csv('weather_train_sid_14.csv', index=False)
df_test_w_sub.to_csv('weather_test_sid_14.csv', index=False)