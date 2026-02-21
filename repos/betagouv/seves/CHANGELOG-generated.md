## Changelog : seves (30 derniers jours)

### Résumé
Les dernières mises à jour de Sèves se concentrent sur l'amélioration des performances, la correction de bugs et l'ajout de nouvelles fonctionnalités pour faciliter la gestion des fiches Seves, des TIAC et des SSA. Des améliorations significatives ont été apportées au chargement massif de documents, à la recherche et à l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Amélioration de la recherche des liens libres via l'API.
- Ajout de la possibilité de masquer des membres de l'équipe dans les sélecteurs.
- Ajout de nouvelles catégories de produits.
- Possibilité d'activer les nouveaux utilisateurs par défaut sur des environnements spécifiques.
- Ajout d'un indicateur pour l'historique des liens sur les SV.
- Amélioration de l'affichage des établissements (enseigne et raison sociale) sur les SSA.
- Ajout de la possibilité de forcer une structure à être disponible comme contact.
- Ajout de nouvelles options de suivi pour les enregistrements simples.
- Correction d'un bug empêchant l'édition des investigations TIAC.
- Correction de la restriction des types de documents lors de l'édition d'un document (#1733).
- Amélioration de l'UX pour le composant LienLibre.
- Ajout d'un mécanisme de verrouillage sur les TIAC et les SSA pour éviter les conflits d'édition.
- Ajout d'une barre de progression pour le chargement massif de documents.
- Correction d'une vulnérabilité XSS dans la fonctionnalité de chargement massif de documents.
- Amélioration de la détection du type MIME pour les fichiers docx.
- Suppression des messages d'erreur vides lors du chargement massif de documents.
- Amélioration de la gestion des erreurs et du feedback visuel lors du chargement massif de documents.
- Ajout de la possibilité de limiter la création de TIAC/SSA.
- Amélioration de l'affichage des badges pour le nombre de participants sur les TIAC.
- Ajout de Saint-Pierre-et-Miquelon à la liste des départements.

### Évolutions techniques
- Refactorisation du code pour préparer le support du chargement massif de documents asynchrone.
- Utilisation de `ruff` pour le tri des imports.
- Amélioration des performances globales de l'application.
- Optimisation des performances des pages de listes pour les TIAC et les SSA.
- Optimisation des requêtes pour l'affichage des listes d'objets TIAC.
- Amélioration des tests unitaires pour les documents.
- Mise à jour de plusieurs dépendances : Django, django-environ, filelock, pytest-django, redis, ruff, urllib3, django-dirtyfields, django-debug-toolbar, sentry-sdk[django], playwright.
- Ajout du paramètre `--fix` au hook `ruff` dans `pre-commit`.
- Utilisation d'une nouvelle fork pour `docxcompose`.
- Harmonisation des dates entre les TIAC et les SSA.
- Suppression des éléments en double dans la recherche de texte libre.
- Ajout d'alertes/warnings pour l'équipe sur l'environnement de production.
- Ajout d'une variable d'environnement pour contrôler l'envoi des emails d'accès.
- Amélioration des performances des pages de mise à jour.
- Correction de la détection incorrecte du type MIME pour certains fichiers XLS.
- Ajout de sauts de ligne pour les évaluations sur les ICH.
- Mise à jour de la configuration de Django pour permettre l'utilisation de partials dans les templates de formulaires.

### Autres changements
- Suppression d'un ancien flag de fonctionnalité.
- Modification du nombre d'objets affichés sur les pages de liste.
- Correction de bugs liés à l'affichage des dates.
- Amélioration des tests pour les listes SSA.
- Suppression de la règle pour le champ RASFF sur les SSA.
- Modification des types de documents pour les TIAC.
- Correction d'un test flaky lors de l'affichage de plusieurs modèles avec le même ID.
- Remplacement des URL par du texte dans les notifications par email.
- Ajout de la possibilité d'ajouter des contacts MUS si le suivi concerne un MUS.
- Séparation du champ "numero" en deux champs distincts.
- Limitation du nombre de caractères dans le nom de fichier pour les documents.
