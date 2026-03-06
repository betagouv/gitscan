# Synthèse d'activité : MTES-MCT (derniers 7 jours)

## Résumé de l'activité
L'organisation MTES-MCT a connu une semaine riche en activités, avec des mises à jour significatives sur de nombreux dépôts. Les efforts se sont concentrés sur l'amélioration de la sécurité (notamment sur *mobilic* et *verseau2*), l'enrichissement des données ( *ecobalyse-data*, *fisheries-and-environment-data-warehouse*), et l'amélioration de l'expérience utilisateur ( *Dossier-Facile-Frontend*, *envergo*, *monitor-ui*). Plusieurs projets ont bénéficié de refactorisations techniques importantes, comme *Lucca* et *mobilic*, visant à améliorer la maintenabilité et la performance. Des nouvelles fonctionnalités ont été ajoutées à *Docurba*, *Lucca*, *acceslibre*, *carbure*, *dialog*, *fonds-prevention-argile* et *potentiel*, offrant ainsi de nouvelles capacités aux utilisateurs.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- *mobilic* : Restriction de l'accès à l'authentification ProConnect pour les contrôleurs.
- *verseau2* : Migration vers une nouvelle architecture d'authentification et correction de failles de sécurité.
- *td-mass-validator* : Amélioration de la validation des fichiers d'import.
- *vizeau* : Mise à niveau d'Adonis pour corriger des failles de sécurité.

## Autres changements notables
Plusieurs refactorisations et migrations importantes ont eu lieu :

- *Lucca* : Refactorisation de `AdherentController` et `DataTableTrait`.
- *acceslibre* : Migration de Bootstrap vers le DSFR.
- *mobilic* : Refonte de l'architecture et migration vers de nouvelles technologies.
- *verseau2* : Refonte de l'authentification et migration vers MASA.
- *td-mass-validator* : Migration vers une nouvelle architecture.
- *trackdechets-vigiedechets* : Amélioration de l'architecture et ajout de nouvelles fonctionnalités.

Des changements d'infrastructure notables ont également été effectués sur *envergo* et *monitorenv*.

## Dépôts les plus actifs
Voici les dépôts les plus actifs de la semaine :

- [Docurba](/repos/MTES-MCT/Docurba) : Amélioration de la gestion des procédures et des événements, correction de bugs.
- [Dossier-Facile-Frontend](/repos/MTES-MCT/Dossier-Facile-Frontend) : Corrections de bugs, améliorations de l'accessibilité et de l'interface utilisateur.
- [Lucca](/repos/MTES-MCT/Lucca) : Ajout de la possibilité de cloner un adhérent, amélioration du formulaire de département.
- [acceslibre](/repos/MTES-MCT/acceslibre) : Ajout de la possibilité d'ajouter une image aux ERPs, migration vers le DSFR.
- [carbure](/repos/MTES-MCT/carbure) : Ajout de la gestion du biogaz et du biométhane, amélioration de l'interface utilisateur.
- [mobilic](/repos/MTES-MCT/mobilic) : Refonte de l'interface d'administration, amélioration de la sécurité.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Ajout de la planification des tâches et de la gestion des tags d'exploitation.
- [verseau2](/repos/MTES-MCT/verseau2) : Refonte de l'authentification, ajout de nouveaux contrôles.
