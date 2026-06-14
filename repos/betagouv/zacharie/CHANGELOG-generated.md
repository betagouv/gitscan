## Changelog : zacharie (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Zacharie en se concentrant sur l'expérience utilisateur, notamment pour les chasseurs et les administrateurs. Des corrections de bugs et des améliorations de l'interface ont été apportées, ainsi que des fonctionnalités pour la gestion des carcasses et des FEI (Fiches d'Évaluation Initiale). Des efforts ont également été déployés pour optimiser les performances et la sécurité de l'application.

### Évolutions fonctionnelles
- Amélioration de l'affichage de l'entité "premier détenteur" au lieu de la personne sur les fiches [#442](https://github.com/betagouv/zacharie/issues/442).
- Ajout d'un filtre "Saison" (1er juin - 31 mai) sur les pages de fiches [#427](https://github.com/betagouv/zacharie/issues/427).
- Possibilité de modifier le numéro de bracelet ou d'ajouter une carcasse à un examen initial [#383](https://github.com/betagouv/zacharie/issues/383).
- Les carcasses sont maintenant regroupées par destinataire dans la vue chasseur [#409](https://github.com/betagouv/zacharie/issues/409).
- Ajout d'un bouton pour supprimer un utilisateur en tant qu'administrateur [#429](https://github.com/betagouv/zacharie/issues/429).
- Gestion du statut "clôturée" d'une FEI via ses carcasses [#414](https://github.com/betagouv/zacharie/issues/414).
- Page listant les utilisateurs ayant interagi avec l'ETG (Évaluation Technique du Gibier) [#415](https://github.com/betagouv/zacharie/issues/415).
- Affichage des sous-totaux de carcasses par espèce [#424](https://github.com/betagouv/zacharie/issues/424).
- Amélioration de l'interface utilisateur pour les carcasses [#373](https://github.com/betagouv/zacharie/issues/373).
- Amélioration de l'interface pour la création d'associations de chasse pour l'onboarding et le profil [#380](https://github.com/betagouv/zacharie/issues/380).

### Évolutions techniques
- Refonte de la gestion des rôles utilisateurs, empêchant un utilisateur de changer son propre rôle [#416](https://github.com/betagouv/zacharie/issues/416).
- Changement de la méthode de chargement des données, passant par les carcasses au lieu des fiches pour optimiser les performances [#392](https://github.com/betagouv/zacharie/issues/392).
- Nettoyage du code et suppression de code obsolète, notamment concernant l'ancien tableau de bord [#391](https://github.com/betagouv/zacharie/issues/391) et le code legacy tipimail [#425](https://github.com/betagouv/zacharie/issues/425).
- Ajout de prettier dans le workflow de CI/CD pour assurer la cohérence du code [#393](https://github.com/betagouv/zacharie/issues/393).
- Optimisation des appels et de la gestion des filtres [#390](https://github.com/betagouv/zacharie/issues/390).
- Mise en place de tests de non-régression pour préparer le changement de récupération des données [#384](https://github.com/betagouv/zacharie/issues/384).
- Amélioration de la gestion du cache et de la déconnexion des utilisateurs [#402](https://github.com/betagouv/zacharie/issues/402).

### Autres changements
- Ajout de documentation pour les emails [#422](https://github.com/betagouv/zacharie/issues/422).
- Mise à jour de la documentation claude.md [#434](https://github.com/betagouv/zacharie/issues/434).
- Ajout d'un tracker pour les pages 404 [#420](https://github.com/betagouv/zacharie/issues/420).
- Amélioration du design des pages de détails administrateur [#430](https://github.com/betagouv/zacharie/issues/430).
- Ajout d'un bandeau pour le Gamefair [#412](https://github.com/betagouv/zacharie/issues/412).
- Correction de l'affichage du destinataire choisi par le premier détenteur [#423](https://github.com/betagouv/zacharie/issues/423).
- Correction de bugs liés à l'onboarding et à l'examen initial [#422](https://github.com/betagouv/zacharie/issues/422).
- Correction de bugs concernant l'affichage des informations des membres [#443](https://github.com/betagouv/zacharie/issues/443).
- Correction de bugs liés au mailing d'onboarding [#428](https://github.com/betagouv/zacharie/issues/428).
- Amélioration de la gestion du scroll to top pour le quiz [#420](https://github.com/betagouv/zacharie/issues/420).
- Correction du quiz Gamefair [#437](https://github.com/betagouv/zacharie/issues/437).
- Mise à jour des scopes des départements utilisateurs [#411](https://github.com/betagouv/zacharie/issues/411).
- Ajout de specs pour la gestion de la trichine [#389](https://github.com/betagouv/zacharie/issues/389).
- Correction de faux positifs dans les alertes Sentry [#417](https://github.com/betagouv/zacharie/issues/417).
- Correction de problèmes d'affichage responsive des formulaires d'adresse [#403](https://github.com/betagouv/zacharie/issues/403).
- Amélioration du style du dashboard chasseur [#401](https://github.com/betagouv/zacharie/issues/401).
- Correction de l'affichage des labels de date [#396](https://github.com/betagouv/zacharie/issues/396).
- Ajout d'un redirect pour les pages 404 [#420](https://github.com/betagouv/zacharie/issues/420).
- Mise en place d'un cron pour relancer la complétion de profil [#430](https://github.com/betagouv/zacharie/issues/430).
- Layout de la sidebar admin [#440](https://github.com/betagouv/zacharie/issues/440).
