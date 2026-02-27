## Changelog : monitorfish (30 derniers jours)

### Résumé
Les dernières mises à jour de monitorfish se concentrent sur l'amélioration de la gestion des infractions, des rapports d'activité (Act-Rep), des groupes de navires et de la surveillance des alertes. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment au niveau de l'affichage des données et de la gestion des filtres. Des travaux de maintenance technique ont également été réalisés, incluant des mises à jour de dépendances et des améliorations de l'infrastructure.

### Évolutions fonctionnelles
- Ajout d'un bouton radio "Contrôle INN" dans le formulaire de contrôle (#4858).
- Affichage d'une pastille sur l'onglet de la fiche navire en cas de signalement (#4853).
- Mise à jour de l'Act-Rep MED (#4816).
- Ajout de la possibilité de télécharger les groupes de navires depuis le menu carto (#4802).
- Affichage des groupes de navires sur la carte en fonction des filtres appliqués (#4800).
- Correction de l'affichage de la note de probabilité (#4817).
- Correction d'une erreur de formattage sur le champ `gearOnboard` des RTP (#4815).
- Correction des retouches sur le filtre par zone pour les groupes de navires (#4814).
- Suppression des infractions "en attente" dans les préavis diffusés (#4826).
- Ajout d'événements Matomo pour le suivi des alertes (#4852) et des signalements (#4844).
- Correction de l'affichage des infractions "en attente" comme étant "à compléter" (#4834).
- Ajout des catégories d'infractions avec corrections UI (#4825).
- Ajout de la possibilité de masquer les pastilles des groupes dans les étiquettes (#4788).

### Évolutions techniques
- Rétablissement des requêtes et des connexions aux bases Oracle (#4868, #4865).
- Activation du mode "thick" pour la base de données Oracle (#4868).
- Mise à jour de la version de Webpack dans le frontend (#4851, #4806).
- Mise à jour de la version de `@jest/globals` dans le frontend (#4806, #4805).
- Mise à jour de la version de `hibernate-spatial` dans le backend (#4809).
- Mise à jour de la version de `cypress-io/github-action` (#4813).
- Amélioration des performances du rendu des groupes de navires.
- Correction de problèmes de sérialisation.
- Suppression de la dépendance KeplerGL.
- Passage de cx_oracle à oracledb.
- Correction de la détection de liens morts dans l'email de vérification de la rég (#4840).
- Mise à jour des dépendances Python dans le pipeline (#4765, #4763).
- Correction de bugs et amélioration des tests Cypress.
- Mise à jour des URLs du registre Docker.
- Amélioration de la gestion des logs Docker.
- Correction de problèmes de typage TypeScript.

### Autres changements
- Documentation mise à jour (#4809).
- Nettoyage du code et application du linter.
- Correction de tests unitaires.
- Ajout de la table ISR et exportation des codes ISR avec l'Act-Rep.
- Suppression de composants obsolètes.
- Correction de problèmes de performance et d'affichage.
- Mise à jour de la version de monitorenv pour les tests Puppeteer.
- Correction de tests unitaires.
- Mise à jour de la version de Prefect (downgrade).
- Ajout de la gestion du code ISR.
