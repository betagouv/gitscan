## Changelog : nosgestesclimat (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante dans la personnalisation des simulations grâce à l'intégration de l'âge et des lieux de vie dans le profil utilisateur. De nombreuses corrections ont également été apportées aux règles de calcul, notamment pour les mineurs et les utilisateurs résidant en Suisse, afin de garantir une précision accrue des résultats de l'empreinte carbone.

### Évolutions fonctionnelles
- **Personnalisation du profil** : Ajout de l'âge et des lieux de vie pour affiner les simulations et les personas [#2826](https://github.com/incubateur-ademe/nosgestesclimat/pull/2826).
- **Précision des règles métier** :
    - Correction massive des règles applicables aux mineurs (énergie, chauffage, isolation, conduite, etc.).
    - Amélioration de la logique de covoiturage pour les longues distances [#2822](https://github.com/incubateur-ademe/nosgestesclimat/pull/2822).
    - Ajustement des conditions de calcul pour les vols et la surface des logements.
- **Adaptation géographique** : Correction des données pour la Suisse afin de supprimer les informations spécifiques à la France [#2832](https://github.com/incubateur-ademe/nosgestesclimat/pull/2832).

### Évolutions techniques
- **Refactorisation des données** : Réorganisation de la question sur l'âge pour l'intégrer dans une catégorie "profil" plus cohérente.
- **Optimisation du moteur de règles** : Introduction de variations pour améliorer la fiabilité de l'exécution des actions de simulation.
- **Workflow** : Correction du workflow DLUO.

### Autres changements
- **Localisation** : Mise à jour de plusieurs traductions (notamment sur le tabac) et corrections de diverses coquilles.
