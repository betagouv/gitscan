## Changelog : vizeau (30 derniers jours, au 06 août 2026)

### Résumé
Ce mois a été marqué par une évolution majeure de l'accessibilité de la plateforme avec l'introduction d'un accès public et d'une nouvelle page d'accueil. L'expérience utilisateur a été enrichie par de nouveaux éléments visuels et une gestion plus fine des projets, désormais partagés entre les territoires. Parallèlement, des travaux importants ont été menés pour stabiliser l'affichage cartographique et moderniser l'architecture interne du logiciel.

### Évolutions fonctionnelles
- **Ouverture publique** : Mise en place d'un accès public incluant une nouvelle page d'accueil, une page de bienvenue et une gestion dédiée des routes pour les visiteurs. [#482](https://github.com/MTES-MCT/vizeau/pull/482)
- **Gestion des projets** : Évolution du modèle métier pour permettre aux projets d'être communs à plusieurs territoires. [#481](https://github.com/MTES-MCT/vizeau/pull/481)
- **Amélioration de l'interface (UI/UX)** : 
    - Intégration d'animations d'apparition au défilement (scroll).
    - Ajout de nouvelles illustrations et de composants de section pour la page d'accueil.
- **Corrections de gestion et droits** :
    - Les commentaires sur les parcelles sont désormais individuels et propres à chaque utilisateur. [#474](https://github.com/MTES-MCT/vizeau/pull/474)
    - Correction des permissions pour le téléchargement des documents de journal de bord. [#477](https://github.com/MTES-MCT/vizeau/pull/477)
    - Amélioration de l'affichage des messages d'erreur lors de l'authentification. [#472](https://github.com/MTES-MCT/vizeau/pull/472)

### Évolutions techniques
- **Stabilité cartographique** : Correction d'un bug critique : les erreurs lors de l'affichage de la carte ne provoquent plus le plantage de l'intégralité de l'application. [#484](https://github.com/MTES-MCT/vizeau/pull/484)
- **Refactorisation de l'architecture** :
    - Migration vers un nouveau système de routage. [#478](https://github.com/MTES-MCT/vizeau/pull/478)
    - Optimisation de la structure du code via l'utilisation de "barrel controllers" et la simplification des modèles. [#476](https://github.com/MTES-MCT/vizeau/pull/476)
    - Automatisation des imports pour les contrôleurs et les politiques de sécurité (policies). [#475](https://github.com/MTES-MCT/vizeau/pull/475)
- **Qualité logicielle** : Diverses corrections et mises à jour de la suite de tests.

### Autres changements
- Nettoyage général du code et corrections de typographies.
- Mise en conformité du formatage de code (Prettier).
