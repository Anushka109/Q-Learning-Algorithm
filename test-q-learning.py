print("Mean reward per thousand episodes")
for i in range(10):
    print("(i+1)*1000,": mean espiode reward: ",\
           np.mean(rewards_per_episode[1000*i:1000*(i+1)]))
