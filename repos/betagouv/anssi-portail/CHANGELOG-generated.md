## Changelog : anssi-portail (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois a été marqué par une transformation majeure du portail. Nous avons lancé de nouveaux outils interactifs, notamment le test d'exposition et des mini-tests (type "Vrai ou Faux"), permettant aux utilisateurs d'évaluer leur niveau de cybersécurité de manière ludique. Parallèlement, l'ensemble du site a bénéficié d'une refonte visuelle complète et d'une modernisation technologique profonde pour offrir une expérience plus fluide et performante.

### Évolutions fonctionnelles
- **Nouveau test d'exposition** : Mise en ligne d'une page dédiée comprenant un radar d'exposition animé, des badges de progression et la possibilité pour les utilisateurs de laisser des réactions et des avis.
- **Nouveaux mini-tests** : Introduction de tests rapides (notamment le format "Vrai ou Faux") avec affichage du score final, animations de célébration (confettis) et suivi des statistiques de réalisation.
- **Amélioration du parcours de sécurisation** : 
    - Ajout de modales de félicitations lors de la complétion de modules ou du parcours complet.
    - Intégration de tutoriels et de nouveaux éléments visuels (pictogrammes, illustrations animées).
    - Meilleure gestion de la progression avec l'attribution de badges.
- **Refonte visuelle (Design System)** : Application d'une nouvelle charte graphique sur l'ensemble du portail (nouveaux motifs de fond, nouveaux composants "Héros", et mise à jour de l'interface utilisateur).
- **Navigation et contenu** : 
    - Amélioration du fil d'Ariane pour une meilleure orientation.
    - Mise à jour des contenus relatifs à la directive NIS2 et aux guides de bonnes pratiques.
    - Optimisation de l'affichage sur mobile pour les parcours et les tests.

### Évolutions techniques
- **Migration vers Svelte 5** : Refonte massive de l'architecture front-end avec la migration de la quasi-totalité des composants vers Svelte 5 et l'activation du mode "runes".
- **Refonte de l'API et du suivi** : 
    - Création de nouvelles routes API pour la gestion des tests, des réponses et des réactions utilisateurs.
    - Mise en place d'un système de suivi des événements (via Brévo) pour analyser les parcours et les complétions de modules.
- **Optimisation et nettoyage** : 
    - Nettoyage approfondi du code : suppression de nombreux composants, styles CSS, images et dépendances inutilisés.
    - Amélioration de la gestion des erreurs et de la robustesse des middlewares.
    - Optimisation des performances de rendu et de la gestion des animations.
- **Infrastructure et CI/CD** : Mise à jour des outils de build (pnpm, Vite) et amélioration des processus de vérification de la qualité du code.

### Autres changements
- **SEO et visibilité** : 
    - Optimisation des URLs (suppression des extensions `.html`).
    - Mise à jour du sitemap et ajout de dates de modification pour améliorer le référencement.
    - Harmonisation des balises méta pour le partage social.
- **Documentation** : Ajout du fichier `llms.txt` pour les outils d'IA.
