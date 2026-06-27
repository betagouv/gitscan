## Changelog : code-du-travail-numerique (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'outil de recherche de conventions collectives avec l'ajout de la recherche d'accords d'entreprise, des corrections de bugs et des améliorations de l'expérience utilisateur, notamment concernant la contribution et l'affichage des informations. Un nouveau système d'extraction et de vérification des événements statiques a également été mis en place.

### Évolutions fonctionnelles
- Ajout de la recherche d'accords d'entreprise dans l'outil "Trouver sa CC" ([#7260](https://github.com/SocialGouv/code-du-travail-numerique/issues/7260)).
- Amélioration du calcul du SMIC annuel avec de nouvelles méthodes de calcul ([#7286](https://github.com/SocialGouv/code-du-travail-numerique/issues/7286)).
- Correction de l'affichage des en-têtes de tableaux dans la section contribution ([#7325](https://github.com/SocialGouv/code-du-travail-numerique/issues/7325)).
- Correction d'un bug empêchant l'ouverture de la page de recherche ([#7293](https://github.com/SocialGouv/code-du-travail-numerique/issues/7293)).
- Correction de l'affichage de l'astérisque sur le brut dans la section contribution ([#7288](https://github.com/SocialGouv/code-du-travail-numerique/issues/7288)).
- Correction d'une erreur dans l'affichage du SMIC dans la section contribution.
- Correction d'un problème d'affichage du code IDCC 9999 dans les conventions collectives ([#7303](https://github.com/SocialGouv/code-du-travail-numerique/issues/7303)).
- Ajout d'un type "bon à savoir" dans la section contribution ([#7326](https://github.com/SocialGouv/code-du-travail-numerique/issues/7326)).
- Correction pour ne plus exiger un minimum d'ancienneté pour le particulier employeur ([#7314](https://github.com/SocialGouv/code-du-travail-numerique/issues/7314)).
- Ajout de logs pour les erreurs d'API dans la section accord.
- Mise en place d'un système d'extraction et de vérification des événements statiques ([#7300](https://github.com/SocialGouv/code-du-travail-numerique/issues/7300)).
- Correction de la redirection de l'ancienne fiche canicule vers la nouvelle page.
- Correction d'un HTML invalide sur les actualités de la page d'accueil.
- Les accords sont maintenant ordonnés par date de signature.

### Évolutions techniques
- Découplage de l'affichage des accords de la recherche d'entreprise pour améliorer la performance et la maintenabilité.
- Adaptation des tests E2E pour le glossaire et la recherche d'en-têtes, et fiabilisation des tests pour les conventions collectives ([#7319](https://github.com/SocialGouv/code-du-travail-numerique/issues/7319)).
- Mise à jour des secrets pour l'environnement de pré-production.

### Autres changements
- Mise à jour des dépendances du projet ([#7297](https://github.com/SocialGouv/code-du-travail-numerique/issues/7297)).
- Correction des tests unitaires suite aux modifications du 1er juin.
- Suppression de la balise canonical sur la page générique de contribution ([#7316](https://github.com/SocialGouv/code-du-travail-numerique/issues/7316)).
- Ajout du support de l'inaptitude pour les assistants maternels de la 3239.
