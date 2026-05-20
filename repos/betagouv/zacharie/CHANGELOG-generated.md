## Changelog : zacharie (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, l'application Zacharie a connu des améliorations significatives sur l'interface utilisateur et l'expérience utilisateur, notamment concernant la gestion des carcasses et des fiches. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application, ainsi que la préparation du déploiement sur un nouvel environnement.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur et de l'expérience utilisateur pour la gestion des carcasses ([#373](https://github.com/betagouv/zacharie/issues/373)).
- Ajout d'une page dédiée aux carcasses ([#353](https://github.com/betagouv/zacharie/issues/353)).
- Implémentation d'un quiz pour le prélèvement et l'assiette ([#361](https://github.com/betagouv/zacharie/issues/361)).
- Ajout d'une liste de lésions ([#331](https://github.com/betagouv/zacharie/issues/331)).
- Ajout d'en-têtes spécifiques pour les fiches SVI et FEI ([#323](https://github.com/betagouv/zacharie/issues/323), [#319](https://github.com/betagouv/zacharie/issues/319)).
- Amélioration de l'affichage des commentaires des intermédiaires dans les modales ([#358](https://github.com/betagouv/zacharie/issues/358)).
- Correction pour permettre aux chasseurs de voir les destinataires des fiches de leur association ([#378](https://github.com/betagouv/zacharie/issues/378)).
- Correction pour empêcher la création de fiches par les simples chasseurs ([#375](https://github.com/betagouv/zacharie/issues/375)).
- Correction pour afficher correctement le nombre total de carcasses ([#344](https://github.com/betagouv/zacharie/issues/344)).
- Correction du calcul du BPH ([#326](https://github.com/betagouv/zacharie/issues/326), [#318](https://github.com/betagouv/zacharie/issues/318)).
- Correction de l'affichage de l'UI de la carte des carcasses ([#312](https://github.com/betagouv/zacharie/issues/312)).
- Correction du scroll-to-top de la navbar ([#322](https://github.com/betagouv/zacharie/issues/322)).
- Correction de l'UI de la liste des fiches ([#302](https://github.com/betagouv/zacharie/issues/302)).

### Évolutions techniques
- Préparation du renversement du GET fei vers GET carcasses avec des tests de non régression ([#384](https://github.com/betagouv/zacharie/issues/384)).
- Nettoyage des contrôleurs et des fonctions de synchronisation ([#382](https://github.com/betagouv/zacharie/issues/382), [#371](https://github.com/betagouv/zacharie/issues/371)).
- Simplification du contrôleur utilisateur ([#364](https://github.com/betagouv/zacharie/issues/364)).
- Suppression de code legacy ([#368](https://github.com/betagouv/zacharie/issues/368)).
- Split du contrôleur admin ([#369](https://github.com/betagouv/zacharie/issues/369)).
- Correction du timeout du cache pour éviter les problèmes de commutation d'utilisateur ([#379](https://github.com/betagouv/zacharie/issues/379)).
- Correction du reset du store à la déconnexion ([#385](https://github.com/betagouv/zacharie/issues/385)).
- Mise à jour de l'URL de base pour l'environnement de staging ([#350](https://github.com/betagouv/zacharie/issues/350)).
- Implémentation d'un système de bearer token pour les appels API ([#336](https://github.com/betagouv/zacharie/issues/336)).
- Amélioration de la gestion des images stockées localement ([#328](https://github.com/betagouv/zacharie/issues/328)).
- Pagination des carcasses pour améliorer les performances ([#329](https://github.com/betagouv/zacharie/issues/329)).

### Autres changements
- Nettoyage des vieux liens du backend ([#372](https://github.com/betagouv/zacharie/issues/372)).
- Correction de l'invitation pour les chasseurs ([#377](https://github.com/betagouv/zacharie/issues/377)).
- Correction du toggle admin ([#376](https://github.com/betagouv/zacharie/issues/376)).
- Correction d'un problème de flaky tests ([#352](https://github.com/betagouv/zacharie/issues/352)).
- Mise à jour de la documentation des tests E2E ([#340](https://github.com/betagouv/zacharie/issues/340), [#334](https://github.com/betagouv/zacharie/issues/334)).
- Correction de messages d'erreur ([#365](https://github.com/betagouv/zacharie/issues/365), [#341](https://github.com/betagouv/zacharie/issues/341)).
- Suppression d'une grosse image ([#335](https://github.com/betagouv/zacharie/issues/335)).
- Correction de l'initialisation du chemin d'accès ([#338](https://github.com/betagouv/zacharie/issues/338)).
- Ajout d'un bouton de connexion pour l'utilisateur administrateur.
