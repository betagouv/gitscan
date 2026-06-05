## Changelog : complements-alimentaires (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur pour la gestion des décisions de visa, notamment en termes de pré-remplissage, de persistance des données et d'affichage. Des corrections ont également été apportées pour améliorer l'expérience utilisateur et la conformité aux standards d'accessibilité (RGAA). Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Évolutions fonctionnelles
- Amélioration de l'interface de modification des décisions de visa : pré-remplissage des valeurs, persistance de la décision lors de la navigation et affichage du délai de réponse. [#2945](https://github.com/betagouv/complements-alimentaires/issues/2945), [#2946](https://github.com/betagouv/complements-alimentaires/issues/2946), [#2947](https://github.com/betagouv/complements-alimentaires/issues/2947)
- Suppression de l'affichage des champs relatifs aux plantes pour les produits qui n'en sont pas. [#2921](https://github.com/betagouv/complements-alimentaires/issues/2921), [#2896](https://github.com/betagouv/complements-alimentaires/issues/2896)
- Amélioration de l'accessibilité : utilisation de listes pour certains éléments de l'interface. [#2942](https://github.com/betagouv/complements-alimentaires/issues/2942)

### Évolutions techniques
- Mises à jour de nombreuses dépendances (Django, Python, Node.js, React, Vue.js, PostgreSQL, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Suppression de la dépendance `ipdb` et ajout de dépendances manquantes. [#2932](https://github.com/betagouv/complements-alimentaires/issues/2932)
- Refactorisation et renommage de composants React liés à la modification des décisions de visa. [#2925](https://github.com/betagouv/complements-alimentaires/issues/2925)

### Autres changements
- Ajustements de marges et d'espacement dans l'interface utilisateur. [#2941](https://github.com/betagouv/complements-alimentaires/issues/2941)
- Amélioration de la réactivité de la grille de colonnes dans le segment de validation de visa. [#2940](https://github.com/betagouv/complements-alimentaires/issues/2940)
