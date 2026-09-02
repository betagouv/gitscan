## Changelog : monitorfish (30 derniers jours, au 01/09/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilisation de la saisie des rapports de contrôle, notamment grâce à une gestion plus fluide de l'auto-sauvegarde et la correction de divers bugs de formulaires. L'expérience utilisateur a également été enrichie par l'affichage des pavillons de navires et l'introduction de questionnaires destinés aux utilisateurs externes.

### Évolutions fonctionnelles
- **Rapports de contrôle & Missions** : Amélioration de l'expérience de saisie avec une auto-sauvegarde plus fluide [#5368], correction de bugs de saisie (poids des espèces [#5362], coordonnées [#fb703aaa], doublons [#5368]) et gestion dynamique de l'affichage des champs (affichage du champ INN [#2203889e] et masquage des maillages [#5367]).
- **Signalements & Profils** : Correction du formulaire de signalement lors du changement de type [#5356], ajout de la possibilité de dupliquer un signalement [#5369] et amélioration de l'affichage des profils de navires (types de segments et familles d'infractions) [#5330].
- **Navigation & AIS** : Affichage du pavillon du navire sur les données AIS [#5410].
- **Utilisateurs externes** : Introduction d'un système de questionnaire via une fenêtre contextuelle (pop-up) pour les utilisateurs externes [#5385, #5387].
- **Préavis** : Correction de l'affichage des diffusions de préavis [#5081] et des notes de correction [#5371].
- **Divers** : Désactivation de l'alerte de suspicion de sous-déclaration [#5382].

### Évolutions techniques
- **Backend & Données** : Recalcul des façades pour les contrôles passés et ajout des façades OM [#5359, #5363], correction des erreurs de timeout JDBC et d'encodage [#5326], et fiabilisation du flux `enrich_lobook_flow` [#5418].
- **Frontend & Tests** : Optimisation de la fréquence des requêtes d'auto-sauvegarde pour réduire la charge serveur [#5368], nettoyage des effets React (timers et listeners) [#5365] et renforcement de la couverture de tests (E2E, Puppeteer, tests de fenêtres latérales) [#2954, #5368].
- **Infrastructure** : Mise à jour de Docker-compose et ajout de clés pour les couches CARTO [#5384].

### Autres changements
- Mise à jour de l'adresse e-mail de contact [#5366].
