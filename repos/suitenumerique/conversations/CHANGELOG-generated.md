## Changelog : conversations (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouvelles fonctionnalités pour l'intégration de modèles open source, l'amélioration de la gestion des documents (support ODT), et l'optimisation de l'interface utilisateur. Des corrections de bugs et des mises à jour de dépendances ont également été effectuées pour améliorer la stabilité et la sécurité du projet.

### Évolutions fonctionnelles
- Ajout du support pour les modèles open source [#1234](https://github.com/suitenumerique/conversations/issues/1234).
- Support de l'analyse des fichiers ODT et amélioration du routage des documents.
- Possibilité de copier le contenu avec le formatage correct pour le coller dans des applications comme Word.
- Ajout d'un bouton de copie qui préserve le formatage.
- Amélioration de l'interface utilisateur pour la gestion des projets.
- Nouvelle interface utilisateur pour l'en-tête.
- Possibilité de taper pendant que le LLM génère une réponse.
- Intégration de snippets de recherche Brave pour améliorer les résultats de recherche.
- Ajout d'un mode débogage pour faciliter le développement local.

### Évolutions techniques
- Refactorisation des tests pour améliorer la qualité du code.
- Mise à jour de Next.js de la version 15 à la version 16.
- Mise à jour des dépendances Python pour bénéficier des dernières corrections et améliorations.
- Suppression des outils de recherche hérités de la configuration du modèle.
- Optimisation du linting du code frontend.
- Amélioration de la gestion des couleurs pour les projets.

### Autres changements
- Mise à jour des chaînes de traduction (i18n).
- Ajout d'une blague pour le 1er avril.
- Mise à jour des descriptions des outils.
- Correction de problèmes de style CSS dans l'interface utilisateur.
- Correction d'un bug empêchant les liens sources de s'ouvrir dans un nouvel onglet.
- Correction d'un bug lié à l'internationalisation (i18n) pour le 1er avril.
- Suppression de l'affichage du "waffle" si le thème n'est pas français.
- Amélioration des performances du rendu Markdown en streaming.
- Correction d'un problème de rendu des formules mathématiques et des traductions.
- Correction de l'inversion des tests de liveness et readiness pour le déploiement backend.
- Correction de problèmes de style en mode sombre pour les messages de chat.
