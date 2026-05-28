## Changelog : maestro (30 derniers jours, au 27 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la gestion des prélèvements, des analyses et des laboratoires, ainsi que par des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur. Des efforts ont également été déployés pour optimiser l'infrastructure et les dépendances du projet.

### Évolutions fonctionnelles
- Possibilité de filtrer les prélèvements par département pour les administrations centrales [#980].
- Ajout d'une interface administrateur pour visualiser toutes les RAI [#898].
- Possibilité de modifier les analytes des laboratoires en PPV [#919].
- Ajout d'un filtre sur les prélèvements avec plusieurs exemplaires [#850, #823].
- Synchronisation des modifications d'utilisateurs de Maestro avec Brevo [#840].
- Ajout d'un service OIDC local pour l'authentification [#841].
- Gestion améliorée des agréments par type de plan pour les laboratoires [#832].
- Possibilité de dupliquer les prélèvements sur les environnements de tests [#842].
- Amélioration de la gestion des dates et des formats dans les exports DAI [#950].
- Correction de l'affichage des prélèvements pour les administrateurs [#897].
- Ajout du numéro DAP et du code barre échantillon sur les étiquettes [#951].
- Prise en compte des non quantifiables pour Cereco [#945].

### Évolutions techniques
- Mise à jour de nombreuses dépendances (React, TypeScript, Node.js, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Amélioration de la gestion des erreurs Zod avec affichage de la valeur problématique [#820].
- Téléversement automatique des sourcemaps sur Sentry pour faciliter le débogage [#821].
- Refactor de l'API pour supprimer les coerces et améliorer le typage [#817].
- Utilisation de `fast-xml-builder` pour la génération de fichiers XML [#829].
- Amélioration du pipeline CI/CD pour garantir la qualité des releases [#822].
- Ajout de cache pour Playwright afin d'accélérer les tests [#814].
- Correction de l'alerte obsolète concernant le setup de Vitest [#867].

### Autres changements
- Correction de bugs liés à la gestion des statuts d'analyse [#981, #978].
- Correction de l'affichage de la date du prélèvement dans la dernière étape [#979].
- Correction de la réinitialisation de la modale de recevabilité [#977].
- Correction de l'affichage des identifiants de listes Brevo [#901].
- Correction de la recherche de la programmation associée à une matrice [#965].
- Correction du filtrage des prélèvements exportés par année [#964].
- Correction de la gestion des doublons de document ID [#938].
- Correction de l'extraction du numéro d'exemplaire [#937].
- Correction de la gestion des dates dans les exports DAI [#948].
- Correction de la gestion des statuts après l'analyse des échantillons [#947].
- Correction de l'affichage des dates dans les exports XLS [#816].
- Correction de la comparaison de dates [#813].
- Correction de bugs mineurs et améliorations de la documentation.
