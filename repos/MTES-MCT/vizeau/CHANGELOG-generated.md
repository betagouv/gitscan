## Changelog : vizeau (30 derniers jours, au 11 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec l'introduction d'une interface publique et d'une page de bienvenue pour améliorer l'accessibilité. La gestion des données est devenue plus flexible grâce au partage de projets entre territoires, tandis que la confidentialité a été renforcée par la personnalisation des commentaires de parcelles. Enfin, la stabilité de l'outil cartographique a été nettement améliorée pour éviter les interruptions de service.

### Évolutions fonctionnelles
- **Nouvelle interface publique** : Ajout d'une page d'accueil publique avec une page de bienvenue, des illustrations et des animations au défilement. [#482](https://github.com/MTES-MCT/vizeau/pull/482)
- **Gestion des projets** : Les projets sont désormais partagés entre les différents territoires. [#481](https://github.com/MTES-MCT/vizeau/pull/481)
- **Confidentialité des données** : Les commentaires sur les parcelles sont désormais individuels et propres à chaque utilisateur. [#474](https://github.com/MTES-MCT/vizeau/pull/474)
- **Amélioration de la stabilité cartographique** : Un plantage lors de l'affichage de la carte n'entraîne plus l'arrêt de l'ensemble de l'application. [#484](https://github.com/MTES-MCT/vizeau/pull/484)
- **Corrections de permissions et d'erreurs** : 
    - Correction des droits de téléchargement pour les documents de journal de bord. [#477](https://github.com/MTES-MCT/vizeau/pull/477)
    - Amélioration de l'affichage des messages d'erreur, notamment lors de l'authentification. [#472](https://github.com/MTES-MCT/vizeau/pull/472)

### Évolutions techniques
- **Optimisation de la cartographie** : Refactorisation des effets de réconciliation sur la carte principale et simplification de l'API pour améliorer les performances de synchronisation. [#487](https://github.com/MTES-MCT/vizeau/pull/487)
- **Migration du routage** : Passage vers un nouveau système de routage pour l'application. [#478](https://github.com/MTES-MCT/vizeau/pull/478)
- **Refactorisation de l'architecture** :
    - Simplification des modèles et utilisation d'imports générés pour les contrôleurs et les politiques. [#475](https://github.com/MTES-MCT/vizeau/pull/475)
    - Mise en place de "barrel controllers" pour une meilleure organisation du code. [#476](https://github.com/MTES-MCT/vizeau/pull/476)
    - Modularisation de l'interface via la création de composants UI réutilisables (ex: `HomeSection`). [#479](https://github.com/MTES-MCT/vizeau/pull/479)

### Autres changements
- **Qualité du code** : Ajout du linting (`npm run lint`) dans le hook de pré-commit pour garantir la conformité du code.
- **Maintenance** : Diverses corrections de typographies et de formatage (Prettier).
