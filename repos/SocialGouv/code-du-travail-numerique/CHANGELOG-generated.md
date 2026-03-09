## Changelog : code-du-travail-numerique (30 derniers jours)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes de recherche, de gestion des documents et de calcul des indemnités. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application, notamment au niveau des tests et du build. Enfin, des sondages ont été ajoutés pour recueillir les retours des utilisateurs sur les accords d'entreprise.

### Évolutions fonctionnelles
- Amélioration de la recherche pour de meilleurs résultats.
- Suppression de l'étape "contrat" dans le calcul des indemnités, simplifiant ainsi le processus.
- Ajout d'un formulaire de sondage pour recueillir l'avis des utilisateurs sur les accords d'entreprise ([#7121](https://github.com/SocialGouv/code-du-travail-numerique/issues/7121)).
- Modification de la phrase d'accroche du questionnaire sur les accords d'entreprise ([#7126](https://github.com/SocialGouv/code-du-travail-numerique/issues/7126)).
- Ajout d'une question à la recherche pour évaluer la pertinence des résultats ([#7115](https://github.com/SocialGouv/code-du-travail-numerique/issues/7115)).
- Amélioration de la gestion des listes et des informations dans la page des modèles de documents ([#7117](https://github.com/SocialGouv/code-du-travail-numerique/issues/7117)).
- Suppression du questionnaire sur les accords d'entreprise.

### Évolutions techniques
- Optimisation du temps de build Docker ([#7122](https://github.com/SocialGouv/code-du-travail-numerique/issues/7122)).
- Mise à jour vers la dernière version de Next.js ([#7095](https://github.com/SocialGouv/code-du-travail-numerique/issues/7095)).
- Normalisation du widget Indemnité de rupture conventionnelle pour les tests CI.
- Amélioration des tests e2e pour assurer une couverture plus complète et des résultats fiables.
- Suppression du fichier d'analyse CodeQL.
- Mise à jour des vérifications d'URL canoniques pour les chemins des widgets dans les tests.

### Autres changements
- Suppression de la redirection pour les CCs 1031 et 3203 ([#7109](https://github.com/SocialGouv/code-du-travail-numerique/issues/7109)).
- Ajout des widgets en legacy et des nouveaux widgets ([#7096](https://github.com/SocialGouv/code-du-travail-numerique/issues/7096)).
