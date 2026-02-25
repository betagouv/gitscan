## Changelog : gestion-des-subventions-locales (30 derniers jours)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de gestion des catégories de subventions (DETR/DSIL), de robustesse de l'import de données depuis la DN, et d'optimisations de l'interface d'administration. Des corrections de bugs ont également été apportées pour améliorer l'expérience utilisateur, notamment sur les pages de simulation et de gestion des projets. La sécurité a été renforcée avec l'ajout d'une protection contre les attaques par force brute et l'implémentation de l'authentification à deux facteurs pour les utilisateurs staff.

### Évolutions fonctionnelles
- Ajout de la gestion des catégories DETR/DSIL : récupération, affichage et association aux dossiers (#491, #492).
- Possibilité de compléter les dossiers reportés "sans" pièces justificatives via un formulaire dédié (#496, #526).
- Ajout d'un filtre par arrondissement sur les pages listes de dossiers et de projets du Back Office (#522).
- Affichage du nombre de projets dans les listes de projets (#495).
- Ajout du lien vers Tchap (#506).
- Implémentation de l'authentification à deux facteurs (OTP) pour les utilisateurs staff (#537).
- Suppression de la possibilité de s'authentifier avec un nom d'utilisateur et un mot de passe (#523).
- Amélioration de l'interface utilisateur du formulaire de renseignement d'informations pour un dossier reporté "sans" (#503).
- Ajout des champs libres instructeurs dans les "Annotations" (#494).
- Correction pour accepter les taux supérieurs à 100% depuis les annotations DN (#513).
- Suppression de l'onglet "Annotations" remplacé par "Notes" (#507).
- Renommage des messages de succès des projets acceptés et refusés provisoirement (#516).

### Évolutions techniques
- Refactorisation de la relation entre les modèles Dossier et DossierData (#543).
- Déplacement de la relation entre Demarche depuis DossierData vers Dossier (#536).
- Optimisation des performances des pages d'administration de Collegue et FieldMapping (#518).
- Simplification de la modélisation : suppression de FieldMappingForHuman et renommage de FieldMapping (#493).
- Ajout de la librairie django-axes pour la protection contre les attaques par force brute (#524).
- Utilisation de django-json-widget pour l'édition de champs JSON (#515).
- Ajout d'une tâche pour rafraîchir tous les dossiers de toutes les démarches depuis la DN (#538).
- Ajout d'une tâche pour rafraîchir les dossiers d'une démarche depuis une date donnée (#533).
- Amélioration de la robustesse de l'algorithme de récupération des données d'un dossier DN (#501).
- Correction d'un test (#546).
- Correction d'un test flaky (#533).
- Correction de bugs liés à la suppression de projets et de simulations (#529).
- Correction de bugs liés à l'import d'arrondissements (#541).
- Amélioration de la gestion des erreurs 404 (#529).
- Ajout de dates de création et de modification sur Projet et DotationProjet (#504).
- Suppression de code mort (processModal.js) (#534).

### Autres changements
- Ajout de pages d'erreur 403, 404 et 500 conformes au modèle DSFR (#528).
- Copie de la base de données de l'application parente pour la revue d'application (#527).
- Ajout de droits pour les utilisateurs "équipe" pour changer les périmètres des autres utilisateurs (#531).
- Correction de problèmes de migrations (#541).
- Amélioration de la documentation et des commentaires dans le code.
