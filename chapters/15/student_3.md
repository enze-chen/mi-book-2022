(h1:15:s3)=
# Jesse 🐧🐰🥭

**Title**: A New Dielectric Material Must Emerge

```{image} ../../assets/fig/04/RFCV.png
:width: 50%
:align: center
```

**Description**: In order to produce smaller transistors with increased processing power, new dielectric materials must be explored as the limits of silicon dioxide have been reached. Dielectrics are electrical insulators that block the flow of electric charge; such properties are predominant in high dielectric constant(ε) materials. Through the ussage of machine learning applications, researchers are able to narrow high ε compounds that are of interest. I explored the prediction of high ε by utilizing the Random Forest Regressor model, optimizing hyperparamters with GridSearchCV, and featurizing the training data methodically. All materials were queried based on critieria relating to band gap, stabilty, oxides, and non metal via the MaterialsProject. After screening/filtering of data was prefromed and the models were trained, I ran this trained model on my test dataset to gain predicted values of ε. These were then filtered with feature importance to chose ten materials to explore further and run DFT calculations. Leveraging machine learning tools as in this example, will prove to save money, time and reveal a new alternative for SiO2.
