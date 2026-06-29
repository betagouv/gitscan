## Changelog : code-du-travail-numerique (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche de conventions collectives, notamment avec l'ajout de la prise en charge des accords d'entreprise. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant l'affichage des informations et les tests automatisés.

### Évolutions fonctionnelles
- Ajout de la prise en charge des accords d'entreprise dans l'outil "Trouver sa CC" ([#7260](https://github.com/SocialGouv/code-du-travail-numerique/issues/7260)).
- Amélioration de l'affichage des accords, désormais triés par date de signature ([#7313](https://github.com/SocialGouv/code-du-travail-numerique/issues/7313)).
- Ajout d'un nouveau type de contribution : "bon à savoir" ([#7326](https://github.com/SocialGouv/code-du-travail-numerique/issues/7326)).
- Correction d'un bug empêchant l'ouverture de la page de recherche ([#7293](https://github.com/SocialGouv/code-du-travail-numerique/issues/7293)).
- Correction d'un bug lié à l'affichage des en-têtes de tableaux dans la section contribution ([#7325](https://github.com/SocialGouv/code-du-travail-numerique/issues/7325)).
- Correction d'un bug lié à l'affichage du code IDCC 9999 dans les conventions collectives ([#7303](https://github.com/SocialGouv/code-du-travail-numerique/issues/7303)).
- Correction pour ne plus exiger d'ancienneté minimale pour un particulier employeur ([#7314](https://github.com/SocialGouv/code-du-travail-numerique/issues/7314)).
- Redirection de l'ancienne fiche canicule vers la nouvelle page d'information ([#7318](https://github.com/SocialGouv/code-du-travail-numerique/issues/7318) et [#7322](https://github.com/SocialGouv/code-du-travail-numerique/issues/7322)).

### Évolutions techniques
- Ajout d'un système d'extraction d'événements statiques et de vérification de la dérive ([#7300](https://github.com/SocialGouv/code-du-travail-numerique/issues/7300)).
- Amélioration de la gestion des erreurs d'API avec ajout de logs.
- Découplage de l'affichage des accords de la recherche d'entreprise pour une meilleure modularité.
- Correction des tests unitaires suite à des modifications.
- Blocage de l'affichage des informations sans convention collective sélectionnée ([#7232](https://github.com/SocialGouv/code-du-travail-numerique/issues/7232)).

### Autres changements
- Mise à jour des secrets pour l'environnement de pré-production.
- Suppression d'une balise canonical redondante sur la page générique de contribution ([#7316](https://github.com/SocialGouv/code-du-travail-numerique/issues/7316)).
- Correction d'un problème HTML invalide sur la page d'actualités ([#7292](https://github.com/SocialGouv/code-du-travail-numerique/issues/7292)).
- Mise à jour des dépendances ([#7297](https://github.com/SocialGouv/code-du-travail-numerique/issues/7297)).
- Mise à jour de l'action `amannn/action-semantic-pull-request` ([#6780](https://github.com/SocialGouv/code-du-travail-numerique/issues/6780)).
