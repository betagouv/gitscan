## Changelog : nosgestesclimat (30 derniers jours, au 01/10/2026)

### Résumé
Ce mois-ci, le modèle gagne en précision grâce à une meilleure prise en compte du profil des utilisateurs. L'introduction de nouvelles données (âge et lieu de vie) et l'ajustement des règles de calcul pour des situations spécifiques (mineurs, situations familiales) permettent des simulations d'empreinte carbone plus fines et plus justes.

### Évolutions fonctionnelles
- **Enrichissement du profil utilisateur** : Ajout de nouvelles questions permettant de préciser l'âge et le lieu de vie des utilisateurs, affinant ainsi les résultats de simulation. [#2821](https://github.com/incubateur-ademe/nosgestesclimat/pull/2821) [#2826](https://github.com/incubateur-ademe/nosgestesclimat/pull/2826)
- **Amélioration de l'expérience de simulation** : 
    - Intégration du covoiturage sur longue distance. [#2822](https://github.com/incubateur-ademe/nosgestesclimat/pull/2822)
    - Optimisation des descriptions pour les thématiques des vols, du logement et du tabac. [#2824](https://github.com/incubateur-ademe/nosgestesclimat/pull/2824)

### Évolutions techniques
- **Refonte de la logique métier** : Migration de nombreuses conditions (logement, alimentation, services sociétaux) vers le profil utilisateur pour une gestion plus granulaire des règles.
- **Ajustement des règles de calcul (Publicodes)** :
    - Prise en compte des spécificités liées aux mineurs (impact sur l'énergie, le chauffage, l'isolation et le photovoltaïque).
    - Ajustement des conditions basées sur la situation familiale et professionnelle (parentalité, salariat, mobilité scolaire).
    - Ajout d'une condition basée sur le kilométrage.
- **Optimisation du moteur de règles** : Introduction de "variations" pour améliorer le fonctionnement et la stabilité des actions de simulation.

### Autres changements
- **Maintenance et qualité** :
    - Mise à jour des traductions et corrections de typographies.
    - Sortie des versions 4.17.0 et 4.17.1.
