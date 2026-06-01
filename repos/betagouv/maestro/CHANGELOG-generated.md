## Changelog : maestro (30 derniers jours, au 27 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des prélèvements, des analyses et des laboratoires. Les utilisateurs bénéficieront d'une meilleure expérience grâce à des filtres plus précis, des corrections de bugs et de nouvelles fonctionnalités comme la synchronisation des utilisateurs avec Brevo et la gestion des RAI. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un filtre par département pour les administrations centrales dans la liste des prélèvements. [#980](https://github.com/betagouv/maestro/issues/980)
- Possibilité de modifier les analytes des laboratoires en PPV. [#919](https://github.com/betagouv/maestro/issues/919)
- Ajout d'une interface administrateur pour visualiser toutes les RAI (Requêtes d'Analyse Initiale). [#898](https://github.com/betagouv/maestro/issues/898)
- Synchronisation des utilisateurs de Maestro avec Brevo pour une gestion centralisée. [#840](https://github.com/betagouv/maestro/issues/840)
- Autorisation de la duplication des prélèvements sur les environnements de test. [#842](https://github.com/betagouv/maestro/issues/842)
- Suppression de l'affichage de l'email du laboratoire dans les prélèvements. [#838](https://github.com/betagouv/maestro/issues/838)
- Ajout d'un filtre sur les prélèvements avec plusieurs exemplaires. [#850](https://github.com/betagouv/maestro/issues/850)
- Amélioration de la gestion de la conformité des prélèvements, qui n'est plus possible avant la validation de tous les échantillons. [#981](https://github.com/betagouv/maestro/issues/981)
- Correction du statut des analyses lors du passage de "non recevable" à "notification non reçue". [#978](https://github.com/betagouv/maestro/issues/978)
- Ajout du numéro DAP et du code barre échantillon sur les étiquettes. [#951](https://github.com/betagouv/maestro/issues/951)
- Correction de l'affichage des prélèvements pour les administrateurs. [#897](https://github.com/betagouv/maestro/issues/897)

### Évolutions techniques
- Ajout d'un service OIDC local pour une authentification plus flexible. [#841](https://github.com/betagouv/maestro/issues/841)
- Refactorisation de la gestion des dates et ajout de coercions pour assurer la cohérence des données. [#946](https://github.com/betagouv/maestro/issues/946)
- Amélioration de la gestion des erreurs et ajout de logs pour faciliter le débogage de l'API Brevo. [#886](https://github.com/betagouv/maestro/issues/886)
- Mise à jour de nombreuses dépendances pour améliorer la sécurité et les performances.
- Correction de la recherche de la programmation associée à une matrice de prélèvement. [#965](https://github.com/betagouv/maestro/issues/965)
- Correction de la gestion des statuts suite à l'analyse des échantillons. [#947](https://github.com/betagouv/maestro/issues/947)
- Correction de la duplication de la date du prélèvement dans la dernière étape. [#979](https://github.com/betagouv/maestro/issues/979)
- Correction de la réinitialisation de la modale de recevabilité. [#977](https://github.com/betagouv/maestro/issues/977)
- Correction de l'extraction du numéro d'exemplaire en PPV. [#937](https://github.com/betagouv/maestro/issues/937)

### Autres changements
- Correction de l'export des prélèvements pour filtrer par année. [#964](https://github.com/betagouv/maestro/issues/964)
- Correction des identifiants de listes Brevo. [#901](https://github.com/betagouv/maestro/issues/901)
- Correction des document\_id dupliqués dans les DAI. [#938](https://github.com/betagouv/maestro/issues/938)
- Correction de la gestion des non quantifiables dans Cereco. [#945](https://github.com/betagouv/maestro/issues/945)
- Correction de l'affichage des dates DAI et RAI. [#948](https://github.com/betagouv/maestro/issues/948)
- Suppression d'exceljs et ajout d'un test de non régression. [#863](https://github.com/betagouv/maestro/issues/863)
- Mise à jour de la documentation et des configurations.
