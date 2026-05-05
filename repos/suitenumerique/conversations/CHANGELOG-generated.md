## Changelog : conversations (30 derniers jours, au 4 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la compatibilité avec différents modèles d'IA, l'ajout de nouvelles fonctionnalités d'authentification et l'amélioration de l'expérience utilisateur, notamment au niveau de l'interface et de la gestion des documents. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'une option de connexion OIDC silencieuse pour une expérience utilisateur plus fluide. [#59d8f1e](https://github.com/suitenumerique/conversations/commit/59d8f1e)
- Amélioration de la gestion des documents avec l'ajout du support du format ODT et une meilleure gestion du routage des documents. [#5ca595b](https://github.com/suitenumerique/conversations/commit/5ca595b)
- Ajout d'un outil de documentation automatique pour faciliter la compréhension et l'utilisation des fonctionnalités. [#d26a824](https://github.com/suitenumerique/conversations/commit/d26a824)
- Ajout du support pour les modèles open source, élargissant ainsi les options disponibles pour les utilisateurs. [#0606c36](https://github.com/suitenumerique/conversations/commit/0606c36)
- Nouvelle interface utilisateur pour l'en-tête de l'application, améliorant l'esthétique et la navigation. [#77b9b44](https://github.com/suitenumerique/conversations/commit/77b9b44)
- Amélioration de l'interface utilisateur pour les projets, incluant des corrections visuelles et des ajustements de taille. [#63c8e77](https://github.com/suitenumerique/conversations/commit/63c8e77) et [#b8b5630](https://github.com/suitenumerique/conversations/commit/b8b5630)
- Les liens vers les sources s'ouvrent désormais dans un nouvel onglet. [#5183bc4](https://github.com/suitenumerique/conversations/commit/5183bc4)

### Évolutions techniques
- Correction d'un crash lié au streaming avec les APIs compatibles OpenAI. [#9096d9e](https://github.com/suitenumerique/conversations/commit/9096d9e)
- Refactorisation des tests pour une meilleure organisation et maintenabilité. [#ebdb61b](https://github.com/suitenumerique/conversations/commit/ebdb61b) et [#af618c7](https://github.com/suitenumerique/conversations/commit/af618c7)
- Mise à jour des dépendances `lxml` et `pypdf` pour bénéficier des dernières corrections et améliorations. [#da740f6](https://github.com/suitenumerique/conversations/commit/da740f6)
- Mise à jour des dépendances frontend et backend pour corriger des vulnérabilités de sécurité (CVE). [#2496098](https://github.com/suitenumerique/conversations/commit/2496098)
- Ajout d'un mode debug pour faciliter le développement local. [#2c023a7](https://github.com/suitenumerique/conversations/commit/2c023a7)
- Mise à jour de `pydantic-ai` et d'autres packages. [#a41c609](https://github.com/suitenumerique/conversations/commit/a41c609)
- Suppression de la partie "thinking" pour les modèles qui ne supportent pas le raisonnement. [#6bb3135](https://github.com/suitenumerique/conversations/commit/6bb3135)

### Autres changements
- Ajout de tests pour le composant `SourceItem` en frontend. [#890dc10](https://github.com/suitenumerique/conversations/commit/890dc10)
- Mise à jour des descriptions des outils. [#a9f667b](https://github.com/suitenumerique/conversations/commit/a9f667b)
- Récupération des données carbone depuis l'API Albert. [#26a5fa1](https://github.com/suitenumerique/conversations/commit/26a5fa1)
- Amélioration de l'affichage des blocs de code en mode clair. [#f28c468](https://github.com/suitenumerique/conversations/commit/f28c468)
