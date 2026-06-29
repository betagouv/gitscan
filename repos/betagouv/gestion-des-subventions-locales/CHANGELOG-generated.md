## Changelog : gestion-des-subventions-locales (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des projets et des dossiers, ainsi que sur des optimisations techniques pour la performance et la stabilité de l'application. Des améliorations ont été apportées à l'importation de documents, à la gestion des notifications, et à la robustesse du système face à la concurrence.

### Évolutions fonctionnelles
- Correction du formulaire d'avis de la commission DETR [#774](https://github.com/betagouv/gestion-des-subventions-locales/issues/774).
- Amélioration de la sélection de projets sur plusieurs pages [#766](https://github.com/betagouv/gestion-des-subventions-locales/issues/766).
- Initialisation par défaut de l'assiette d'un DotationProjet au finance\_cout\_total [#765](https://github.com/betagouv/gestion-des-subventions-locales/issues/765).
- Le champ enveloppe est maintenant en lecture seule dans l'admin ProjetAction [#762](https://github.com/betagouv/gestion-des-subventions-locales/issues/762).
- Unification de la page de détail d'un projet, pilotée par son état [#753](https://github.com/betagouv/gestion-des-subventions-locales/issues/753).
- Ajout d'une entrée de menu dédiée pour les modèles de publipostage [#750](https://github.com/betagouv/gestion-des-subventions-locales/issues/750).
- Import des dossiers de tous les territoires gérés [#749](https://github.com/betagouv/gestion-des-subventions-locales/issues/749).
- Affichage du périmètre, des dates Turgot et du report dans l'admin [#748](https://github.com/betagouv/gestion-des-subventions-locales/issues/748).
- Possibilité de définir le nom du fichier PDF lors de la notification d'acceptation [#736](https://github.com/betagouv/gestion-des-subventions-locales/issues/736).
- Correction du décochage silencieux des filtres de type ModelMultipleChoiceFilter [#737](https://github.com/betagouv/gestion-des-subventions-locales/issues/737).
- Correction de la perte du curseur des dossiers supprimés sur les pages vides [#742](https://github.com/betagouv/gestion-des-subventions-locales/issues/742).
- Import en masse des documents signés scannés via un upload direct sur S3 [#739](https://github.com/betagouv/gestion-des-subventions-locales/issues/739).

### Évolutions techniques
- Limitation de chaque token du proxy DS à une requête simultanée pour éviter la surcharge [#758](https://github.com/betagouv/gestion-des-subventions-locales/issues/758).
- Priorisation des tâches Celery selon le contexte d'appel pour améliorer la réactivité [#751](https://github.com/betagouv/gestion-des-subventions-locales/issues/751).
- Ajout d'un verrou anti-concurrence sur la synchronisation des dossiers DS pour éviter les conflits [#740](https://github.com/betagouv/gestion-des-subventions-locales/issues/740).
- Activation de la compression WhiteNoise (gzip + Brotli) des fichiers statiques pour améliorer les performances [#757](https://github.com/betagouv/gestion-des-subventions-locales/issues/757).
- Refactorisation de plusieurs composants pour améliorer la maintenabilité et la lisibilité du code.
- Remplacement de FBV et décorateurs par des CBV dans plusieurs vues.
- Ajout de SafeRedirectMixin pour les redirections POST-next/Referer.
- Amélioration de la gestion des erreurs et des timeouts pour la génération de documents.

### Autres changements
- Journalisation des modifications des utilisateurs via l'admin Django [#741](https://github.com/betagouv/gestion-des-subventions-locales/issues/741).
- Correction d'un test flaky CollegueFactory.
- Suppression des rafraîchissements DS bloquants à l'ouverture des modales [#743](https://github.com/betagouv/gestion-des-subventions-locales/issues/743).
- Correction d'une erreur de manifest staticfiles sur l'importmap [#746](https://github.com/betagouv/gestion-des-subventions-locales/issues/746).
- Cache-busting des fichiers JS de l'importmap [#745](https://github.com/betagouv/gestion-des-subventions-locales/issues/745).
- Réduction du header et du footer pour une meilleure expérience utilisateur [#744](https://github.com/betagouv/gestion-des-subventions-locales/issues/744).
- Correction des largeurs de tableaux TipTap dans l'export PDF [#734](https://github.com/betagouv/gestion-des-subventions-locales/issues/734).
