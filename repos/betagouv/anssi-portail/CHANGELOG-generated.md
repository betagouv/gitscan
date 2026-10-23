## Changelog : anssi-portail (30 derniers jours, au 22 octobre 2026)

### Résumé
Cette période a été marquée par un enrichissement majeur de la "Boîte à outils" avec l'ajout de nombreux modèles de documents et de nouveaux contacts. L'expérience de simulation "Réflexes cyber" a été considérablement améliorée grâce à l'ajout de sons et d'animations, tandis que le "Parcours de sécurisation" est désormais mieux intégré et visible sur l'ensemble du portail. Enfin, un nouveau système de blog a été déployé pour faciliter la diffusion de contenus.

### Évolutions fonctionnelles

**Boîte à outils**
- Ajout de nouveaux modèles personnalisés : revue des droits d'accès, revue de comptes utilisateurs, liste d'activités et modification de mots de passe.
- Possibilité de télécharger les modèles de documents (format XLSX).
- Intégration de nouveaux contacts : nationaux, régionaux et sectoriels.
- Mise en place d'un système de retours utilisateurs directement depuis l'interface des outils.

**Réflexes cyber (Simulation)**
- Amélioration de l'immersion avec l'ajout d'ambiances sonores et d'animations (transitions entre événements, pulsations des métriques, apparition des rôles).
- Optimisation de l'interface : meilleure gestion des scores, des instructions sur mobile et ajout d'illustrations pour les événements.

**Parcours de sécurisation**
- Visibilité accrue : le parcours est désormais accessible via le menu, le pied de page, les résultats des tests de maturité et les simulations.
- Amélioration visuelle avec l'ajout d'animations sur les cartes de parcours.

**Blog et Contenu**
- Déploiement d'un nouveau système de blog permettant la lecture d'articles via leur titre (slug) et l'affichage de résumés.
- Ajout d'un système d'avis utilisateurs sur les articles pour recueillir les impressions des lecteurs.

**Tests de maturité et Mini-tests**
- Déploiement de nouveaux modules de tests (composants "Exposition" et "Vrai/Faux").
- Amélioration de la présentation des résultats et de l'interface utilisateur.

### Évolutions techniques

**Architecture et API**
- Réorganisation et simplification des routes API pour les outils, les annuaires et les mini-tests.
- Refactorisation de la logique de manipulation des fichiers Excel (XLSX) et de la gestion du temps (adaptateur horloge).
- Migration vers Express 5.3 et mise à jour de l'infrastructure (GitHub Runner).
- Mise en place du rendu côté serveur (SSR) pour certaines pages et du système de cache pour les articles du blog.

**Qualité et Maintenance**
- Refactorisation importante pour regrouper les fichiers par domaine (annuaire de crise, liste d'activités, modification de mots de passe, etc.).
- Amélioration de la gestion des erreurs avec un composant 404 réutilisable.
- Mise à jour des règles de linting et automatisation du tri des imports.

### Autres changements
- Mise à jour des métadonnées SEO (titres et descriptions pour les réseaux sociaux).
- Nettoyage du code (suppression de commentaires inutiles et de dépendances obsolètes).
- Amélioration de l'accessibilité (prise en compte du mode "mouvement réduit").
