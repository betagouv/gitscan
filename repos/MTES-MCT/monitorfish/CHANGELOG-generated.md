## Changelog : monitorfish (30 derniers jours)

### Résumé
Cette période a été marquée par de nombreuses améliorations et corrections concernant les contrôles, les rapports d'activité (Act-Rep), les groupes de navires et les alertes. Des optimisations de performance et des mises à jour techniques ont également été apportées pour améliorer la stabilité et la maintenabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un bouton radio "Contrôle INN" dans le formulaire de contrôle (#4858).
- Affichage d'une pastille sur l'onglet de la fiche navire pour signaler un signalement (#4853).
- Amélioration de l'affichage de la note de probabilité (#4817).
- Correction d'une erreur de formatage sur le champ `gearOnboard` des RTP (#4815).
- Correction des retouches sur le filtre par zone pour les groupes de navires (#4814).
- Ajout du téléchargement des groupes de navires dans le menu carto (#4802).
- Affichage des groupes de navires sur la carte en fonction des filtres (#4800).
- Suppression de l'œil permettant de masquer les pastilles des groupes dans les étiquettes (#4788).
- Suppression des infractions "en attente" dans les préavis diffusés (#4826).
- Correction de la détection de liens morts dans l'email de vérification de la réglementation (#4840).
- Ajout d'événements Matomo pour le suivi des alertes (#4852) et des signalements (#4844).
- Mise à jour de l'Act-Rep MED (#4816).
- Correction de l'affichage des catégories d'infractions dans les contrôles (#4835).
- Ajout de la possibilité de ne pas exécuter les règles d'alertes n'ayant aucun paramètre défini (#4838).

### Évolutions techniques
- Mise à jour de la version de webpack dans le frontend (#4851, #4806).
- Mise à jour de la version de `@jest/globals` dans le frontend (#4806, #4809).
- Mise à jour de la version de `virtualenv` dans le pipeline (#4763, #4827).
- Mise à jour de la version de `org.hibernate:hibernate-spatial` dans le backend (#4809).
- Mise à jour de la version de `pyarrow` dans le pipeline (#4765).
- Amélioration des performances de rendu des groupes de navires.
- Optimisation de la récupération des données de reporting pour les navires sans position.
- Mise à jour de la version de monitorenv pour les tests Puppeteer.
- Mise à jour des URLs de registre Docker.
- Refactoring du code pour supprimer des composants et des variables inutilisées.
- Correction de problèmes de sérialisation.
- Correction de types dans le frontend.
- Mise à jour des index de la base de données.
- Changement de la méthode d'authentification pour utiliser oracledb au lieu de cx_oracle.
- Suppression de la dépendance keplergl.

### Autres changements
- Mise à jour de la documentation.
- Application de linting pour améliorer la qualité du code.
- Correction de tests unitaires.
- Ajout de tests Cypress.
- Correction de quelques tests Cypress.
- Ajout de code de suivi Matomo.
- Ajout de la table ISR et exportation des codes ISR avec l'Act-Rep.
- Ajout de la gestion des codes ISR.
- Correction de tests unitaires.
- Ajout de la gestion du tri des menaces.
- Correction de problèmes de typage TypeScript.
