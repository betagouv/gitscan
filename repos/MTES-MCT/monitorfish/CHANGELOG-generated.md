## Changelog : monitorfish (30 derniers jours)

### Résumé
Les dernières mises à jour de Monitorfish se concentrent sur l'amélioration de la gestion des groupes de navires, des rapports d'activité (Act-Rep), des alertes et des contrôles. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées, ainsi que des mises à jour techniques pour optimiser les performances et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un bouton radio "Contrôle INN" dans le formulaire de contrôle (#4858).
- Affichage d'une pastille sur l'onglet de la fiche navire pour signaler des informations importantes (#4853).
- Amélioration de l'affichage de la note de probabilité dans le calcul du facteur de risque (#4817).
- Correction du formattage du champ `gearOnboard` dans les rapports RTP (#4815).
- Correction des retouches sur le filtre par zone dans la gestion des groupes de navires (#4814).
- Ajout du téléchargement des groupes de navires dans le menu carto (#4802).
- Affichage des groupes de navires sur la carte en fonction des filtres appliqués (#4800).
- Correction de l'affichage des infractions "en attente" dans les préavis diffusés (#4826).
- Ajout de la possibilité de masquer les pastilles des groupes dans les étiquettes (#4788).
- Mise à jour de l'Act-Rep MED (#4816).
- Ajout de l'affichage des catégories d'infractions dans le formulaire de contrôle (#4835).
- Ajout de suivi Matomo pour les alertes (#4852) et les signalements (#4844).
- Les alertes paramétrables ne s'exécutent plus si aucun paramètre n'est défini (#4838).

### Évolutions techniques
- Mise à jour de la version de webpack dans le frontend (#4851, #4806).
- Mise à jour de la version de @jest/globals dans le frontend (#4806, #4782).
- Mise à jour de la version de virtualenv dans la pipeline (#4763, #4827).
- Mise à jour de la version de hibernate-spatial dans le backend (#4809).
- Utilisation de l'API Geoserver avec mise en cache RTK et ajout de tri (#4800).
- Correction de la détection de liens morts dans l'email de vérification de la rég (#4840).
- Amélioration des performances du rendu des groupes de navires.
- Correction de plusieurs tests unitaires et de tests Cypress.
- Mise à jour de la configuration Docker.
- Refactorisation du code pour supprimer des composants obsolètes et améliorer la lisibilité.
- Correction de problèmes de sérialisation.

### Autres changements
- Mise à jour de la documentation.
- Correction de typos.
- Amélioration de la gestion des types dans le code.
- Ajout de validations pour le formulaire de groupe de navires.
- Mise à jour des référentiels de catégories d'infractions et de codes ISR.
- Ajout de la gestion des codes ISR pour l'Act-Rep.
- Suppression de la dépendance KeplerGL.
- Changement de cx_oracle vers oracledb.
- Ajout de logs pour faciliter le débogage.
