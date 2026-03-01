## Changelog : seves (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Sèves au cours des 30 derniers jours. Les évolutions incluent des corrections de sécurité, des améliorations de l'interface utilisateur pour faciliter la gestion des documents et des événements, ainsi que des optimisations de performance pour une meilleure réactivité de l'application. Des modifications techniques ont également été apportées pour préparer l'implémentation de nouvelles fonctionnalités, notamment le téléchargement massif de documents.

### Évolutions fonctionnelles
- Possibilité d'ajouter des agents dans le champ de copie des destinataires des DI.
- Ajout des numéros de téléphone des agents dans les signatures d'email.
- Amélioration des cartes d'établissement (etablissement).
- Ajout de Saint-Pierre-et-Miquelon dans la liste des départements.
- Possibilité d'activer les nouveaux utilisateurs par défaut sur des environnements spécifiques.
- Ajout d'une option de suivi (FollowUp) pour les EnregistrementSimple.
- Ajout de liens libres avec une API dédiée pour TIAC.
- Possibilité de forcer une structure à être disponible en tant que contact.
- Amélioration de l'historique des investigations TIAC.
- Ajout de nouveaux types de documents pour TIAC.
- Possibilité de masquer les membres de l'équipe dans les listes déroulantes.
- Amélioration de l'affichage des dates dans les TIAC et SSA.
- Correction d'un bug empêchant la recherche correcte dans les listes ChoicesJs.
- Correction d'une vulnérabilité XSS dans le téléchargement massif de documents sur les fiches.
- Correction d'un problème de détection incorrecte des fichiers XLS.
- Ajout d'un indicateur de progression pour le téléchargement massif de documents.
- Correction d'un bug lié aux noms de fichiers trop longs pour les Documents.
- Amélioration de la recherche de liens libres.
- Ajout d'un indicateur pour les liens d'historique sur les SV.
- Amélioration de l'affichage des informations sur les établissements dans les SSA.
- Correction d'un problème de filtrage des agents et des structures pour ICH.
- Amélioration du temps de chargement des pages de détails pour tous les produits.
- Correction d'un bug lié à l'affichage des valeurs de suivi pour les événements simples.

### Évolutions techniques
- Formatage du code JavaScript et CSS avec Biome.
- Refactorisation du code pour préparer l'implémentation du téléchargement massif asynchrone de documents.
- Mise à jour de plusieurs dépendances : Django, django-environ, django-dsfr, sentry-sdk, ruff, sqlparse, virtualenv, urllib3, django-reversion-compare, playwright.
- Ajout du paramètre `--fix` au hook ruff dans pre-commit pour la correction automatique des erreurs de style.
- Configuration du fichier `.editorconfig` pour les fichiers YAML et formatage du fichier `.pre-commit-config.yaml`.
- Utilisation d'une nouvelle fork pour docxcompose.
- Nettoyage de code ancien lié au téléchargement massif synchronisé de documents.

### Autres changements
- Correction d'une vulnérabilité potentielle dans les liens rappel conso.
- Ajout d'une alerte/avertissement pour l'équipe sur l'environnement de production.
- Amélioration des tests unitaires pour les Documents et les listes SSA.
- Modification de l'ordre des champs de filtre dans les TIAC.
- Ajout de sauts de ligne pour les évaluations dans ICH.
- Mise à jour de la configuration de Django pour permettre l'utilisation de partials dans les modèles de formulaire.
- Ajout de nouvelles structures dans l'import agricoll.
- Amélioration des performances globales de l'application.
- Suppression d'un ancien flag de fonctionnalité.
- Correction d'un bug lié à la révision des pages sur SSA/TIAC.
- Modification du titre des pages de mise à jour TIAC.
- Suppression d'éléments en double dans la recherche en texte libre.
- Modification du nombre d'éléments affichés sur les pages de liste.
- Correction d'un bug lié à l'harmonisation des dates entre TIAC et SSA.
- Optimisation de l'API FreeLinks.
- Correction d'un problème lié à la restriction des types de documents lors de la modification d'un document.
