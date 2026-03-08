## Changelog : gestion-des-subventions-locales (30 derniers jours)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment avec l'ajout de fonctionnalités de tri, de filtrage et de personnalisation des tableaux de données. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application, ainsi que des améliorations de sécurité et de performance. L'authentification à deux facteurs a été implémentée pour les utilisateurs staff.

### Évolutions fonctionnelles
- Ajout de la possibilité de réinitialiser l'affichage des colonnes dans les tableaux de données. [#565](https://github.com/betagouv/gestion-des-subventions-locales/issues/565)
- Ajout de la possibilité de filtrer les dossiers et projets par arrondissement dans l'interface d'administration. [#522](https://github.com/betagouv/gestion-des-subventions-locales/issues/522)
- Ajout d'une colonne "N° D.N." avec un lien vers la D.N. dans les tableaux des dossiers, projets et programmations. [#548](https://github.com/betagouv/gestion-des-subventions-locales/issues/548)
- Ajout d'une page permettant d'afficher les projets ayant des annotations manquantes. [#555](https://github.com/betagouv/gestion-des-subventions-locales/issues/555)
- Ajout de la possibilité de supprimer un projet depuis l'interface d'administration Django. [#520](https://github.com/betagouv/gestion-des-subventions-locales/issues/520)
- Ajout d'une vidéo de démonstration sur la page d'aide. [#526](https://github.com/betagouv/gestion-des-subventions-locales/issues/526)
- Implémentation de l'authentification à deux facteurs (OTP) pour les utilisateurs staff. [#537](https://github.com/betagouv/gestion-des-subventions-locales/issues/537)
- Ajout de colonnes "Commentaires" et "Champs libres" (annotations) dans les tableaux. [#563](https://github.com/betagouv/gestion-des-subventions-locales/issues/563)
- Ajout d'une colonne "Assiette" dans les tableaux. [#561](https://github.com/betagouv/gestion-des-subventions-locales/issues/561)
- Amélioration de l'affichage du nombre de décimales pour les taux. [#557](https://github.com/betagouv/gestion-des-subventions-locales/issues/557)
- Correction pour permettre l'acceptation des taux supérieurs à 100% depuis les annotations DN. [#513](https://github.com/betagouv/gestion-des-subventions-locales/issues/513)
- Renommage de l'onglet "Annotations" en "Notes". [#507](https://github.com/betagouv/gestion-des-subventions-locales/issues/507)
- Renommage des messages de succès des projets acceptés et refusés provisoirement. [#516](https://github.com/betagouv/gestion-des-subventions-locales/issues/516)

### Évolutions techniques
- Migration des tableaux vers la structure DSFR et application du nommage BEM. [#544](https://github.com/betagouv/gestion-des-subventions-locales/issues/544)
- Refactorisation du code pour utiliser `BaseModel` au lieu de `TimestampedModel`.
- Optimisation des performances des pages d'administration de `Collegue` et `FieldMapping` en corrigeant les requêtes N+1. [#518](https://github.com/betagouv/gestion-des-subventions-locales/issues/518)
- Déplacement de la relation entre `Dossier` et `DossierData` vers `DossierData`.
- Déplacement de la relation de `Demarche` depuis `DossierData` vers `Dossier`.
- Ajout des dates de création et de modification sur `Projet` et `DotationProjet`. [#504](https://github.com/betagouv/gestion-des-subventions-locales/issues/504)
- Ajout de la possibilité de rafraîchir tous les dossiers de toutes les démarches depuis DN. [#533](https://github.com/betagouv/gestion-des-subventions-locales/issues/533)
- Ajout d'une tâche pour rafraîchir les dossiers d'une démarche depuis une date donnée. [#538](https://github.com/betagouv/gestion-des-subventions-locales/issues/538)
- Ajout d'une protection contre les attaques par force brute avec django-axes. [#524](https://github.com/betagouv/gestion-des-subventions-locales/issues/524)
- Suppression de la connexion par username/mot de passe.
- Correction d'un test flaky.
- Correction de la création des catégories DETR lorsqu'elles ne sont pas trouvées.
- Correction pour éviter la suppression des dotations projets programmés lors d'une mise à jour depuis un dossier DN accepté. [#521](https://github.com/betagouv/gestion-des-subventions-locales/issues/521)

### Autres changements
- Ajout d'identifiants Matomo aux formulaires pour le suivi analytique. [#532](https://github.com/betagouv/gestion-des-subventions-locales/issues/532)
- Ajout de la possibilité de configurer un identifiant Matomo différent pour l'environnement de staging.
- Correction de la persistance de la visibilité des colonnes masquées par défaut. [#564](https://github.com/betagouv/gestion-des-subventions-locales/issues/564)
- Blocage des comptes utilisateurs qui ne se sont pas connectés depuis plus d'un an. [#552](https://github.com/betagouv/gestion-des-subventions-locales/issues/552)
- Correction de problèmes de CSS et d'alignement dans l'interface utilisateur.
- Suppression de code mort.
- Mise à jour de la documentation.
