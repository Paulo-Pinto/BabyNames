import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_file():
    return pd.read_csv("files/NationalNames.csv")


def show_name_by_gender_seaborn(data, name="Jessie"):
    """Shows the distribution of a name by gender

    * Seaborn
    """
    name_data = data[data['Name'] == name]

    plt.title(f"{name}'s by gender (at birth) in the USA")

    # plot name_data by count per year, distinguishing between genders
    sns.lineplot(data=name_data, x="Year", y="Count", hue="Gender")

    # set colours
    colors = ["#d278e3", "#4287f5"]
    sns.set_palette(sns.color_palette(colors))

    plt.show()


def show_name_by_gender(data, name="Jessie"):
    """Shows the distribution of a name by gender

    * Matplotlib
    """
    name_data = data[data['Name'] == name]

    # get years that contain data
    t = [year for year in name_data['Year'].unique()]

    plt.title(f"{name}'s by gender (at birth) in the USA")

    # separate the data into male and female
    males = name_data[name_data['Gender'] == 'M']
    females = name_data[name_data['Gender'] == 'F']

    # add the male and female info to the plot
    plt.plot(t, males['Count'], label="M")
    plt.plot(t, females['Count'], label="F")

    plt.show()


def check_unisex_names(data):
    # TODO : check the most gender-fluid names
    # get all names
    # print(data['Name'].tolist())
    # for name in data:
    #     print(name)
    for index, row in data.head().iterrows():
        print(row['Name'], row['Gender'],
              data[(data['Name'] == row['Name']) & (data['Gender'] != row['Gender']) & (data['Year'] == row['Year'])])
        dataf = data.loc['1']
        print(dataf.head())


if __name__ == '__main__':
    df = read_file()
    # print(df.head())

    name_input = ""
    while name_input := input("Type a name "):
        # make sure the first letter is uppercase
        name_input = name_input[0].upper() + name_input[1:]

        # show_name_by_gender(df, name_input)
        show_name_by_gender_seaborn(df, name_input)

# check_unisex_names(df)


# TODO: investigate what happened to Mac in the 1940s, possibly check state specific data
