## Changelog : pitchou (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur, notamment pour les instructeurs, avec l'ajout de nouvelles fonctionnalités de visualisation de données (cartographie, informations porteur de projet), de gestion des pièces jointes et de filtres. Des corrections et des améliorations de la sécurité ont également été apportées, ainsi que des mises à jour de la documentation et de la configuration.

### Évolutions fonctionnelles
- **Instructeur :** Ajout de la possibilité de contacter le dépositaire du dossier directement depuis l'entête du dossier. [#630](https://github.com/betagouv/pitchou/issues/630)
- **Instructeur :** Ajout d'un onglet "Porteur de projet" pour afficher les informations relatives au porteur de projet. [#627](https://github.com/betagouv/pitchou/issues/627)
- **Instructeur :** Affichage et téléchargement de la cartographie associée au dossier. [#629](https://github.com/betagouv/pitchou/issues/629)
- **Instructeur :** Amélioration de la réactivité de la date des prescriptions et de l'interface utilisateur. [#649](https://github.com/betagouv/pitchou/issues/649)
- **Instructeur :** Rafraîchissement du dossier en cache pour assurer l'affichage des données les plus récentes. [#648](https://github.com/betagouv/pitchou/issues/648)
- **Instructeur :** Ajout de suivi d'audience avec Matomo. [#656](https://github.com/betagouv/pitchou/issues/656)
- **Instructeur :** Activation de la saisie de date typée. [#658](https://github.com/betagouv/pitchou/issues/658)
- **Dossier :** Ajout de nouveaux filtres pour faciliter la recherche et le tri des dossiers. [#645](https://github.com/betagouv/pitchou/issues/645)
- **Dossier :** Remplacement de "representative" par "identite_dossier" pour une meilleure clarté. [#651](https://github.com/betagouv/pitchou/issues/651)
- **Avis :** Ajout de directives pour la prise de décision du CNPN. [#643](https://github.com/betagouv/pitchou/issues/643)
- **Pièces jointes :** Ajout d'une modale pour la gestion des pièces jointes. [#634](https://github.com/betagouv/pitchou/issues/634)
- **Authentification :** Autorisation de domaines de préfecture supplémentaires pour l'accès. [#637](https://github.com/betagouv/pitchou/issues/637), [#641](https://github.com/betagouv/pitchou/issues/641), [#655](https://github.com/betagouv/pitchou/issues/655), [#657](https://github.com/betagouv/pitchou/issues/657)
- **Admin :** Ajout d'une page de suivi des événements. [#664](https://github.com/betagouv/pitchou/issues/664)
- **Admin :** Ajout de liens vers les fichiers et Google Drive dans le tableau de bord. [#660](https://github.com/betagouv/pitchou/issues/660)
- **Admin :** Ajout de la gestion des groupes d'instructeurs. [#633](https://github.com/betagouv/pitchou/issues/633), [#664](https://github.com/betagouv/pitchou/issues/664)
- **Génération de documents :** Ajout du nom du département dans les tags de génération de documents. [#668](https://github.com/betagouv/pitchou/issues/668)
- **Génération de documents :** Mise à jour des modèles de documents et ajout de nouveaux fichiers de saisine. [#652](https://github.com/betagouv/pitchou/issues/652)

### Évolutions techniques
- **Architecture :** Déplacement des pages admin vers l'application Admin. [#622](https://github.com/betagouv/pitchou/issues/622)
- **Authentification :** Implémentation de l'authentification avec ProConnect. [#613](https://github.com/betagouv/pitchou/issues/613)
- **Base de données :** Traduction du schéma de la base de données. [#652](https://github.com/betagouv/pitchou/issues/652)
- **Build :** Mise à jour des dépendances Node.js et pnpm. [#666](https://github.com/betagouv/pitchou/issues/666)
- **Build :** Utilisation des dépendances natives de Just pour éviter les exécutions imbriquées redondantes. [#667](https://github.com/betagouv/pitchou/issues/667)
- **Frontend :** Mise en place de Tailwind CSS en parallèle du DSFR et portage des fichiers. [#665](https://github.com/betagouv/pitchou/issues/665)
- **Frontend :** Application du modèle DSFR à la page de connexion. [#659](https://github.com/betagouv/pitchou/issues/659)
- **Monitoring :** Mise en place de Sentry pour les applications instructeur et admin.
- **Staging :** Réinitialisation de la base de données et de S3 à chaque déploiement. [#621](https://github.com/betagouv/pitchou/issues/621)
- **Refactoring :** Code en anglais avec termes métier français sans accents. [#647](https://github.com/betagouv/pitchou/issues/647)

### Autres changements
- Mise à jour de la documentation des premiers pas.
- Ajout de l'adresse email de contact sur la page 404. [#661](https://github.com/betagouv/pitchou/issues/661)
- Ajout de mentions légales. [#638](https://github.com/betagouv/pitchou/issues/638)
- Mise à jour du délégué à la protection des données (DPO). [#624](https://github.com/betagouv/pitchou/issues/624)
- Nettoyage du code après la migration vers S3. [#598](https://github.com/betagouv/pitchou/issues/598)
- Suppression de la personne qui suit le dossier lorsque celle-ci n'a plus accès au dossier. [#625](https://github.com/betagouv/pitchou/issues/625)
- Correction de la sélection GraphQL geometry pour la synchronisation des données. [#632](https://github.com/betagouv/pitchou/issues/632)
- Correction d'un bug lié à la date des avis. [#653](https://github.com/betagouv/pitchou/issues/653)
- Correction d'un bug lié au déposant/mandataire en personne morale. [#650](https://github.com/betagouv/pitchou/issues/650)
- Ajout de suivi des clics sur les liens de navigation. [#663](https://github.com/betagouv/pitchou/issues/663)
- Ajout du support des fichiers .xlsx. [#628](https://github.com/betagouv/pitchou/issues/628)
