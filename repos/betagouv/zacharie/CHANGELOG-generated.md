## Changelog : zacharie (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Zacharie se concentrent sur l'amélioration de la gestion des transmissions de données entre les différents acteurs (chasseurs, collecteurs, vétérinaires, etc.), la correction de bugs liés à l'interface utilisateur et à la gestion des données, ainsi que l'ajout de nouvelles fonctionnalités pour faciliter l'utilisation de l'application, notamment pour l'administration et le suivi des carcasses.

### Évolutions fonctionnelles
- Amélioration de la gestion des transmissions pour les chasseurs et les collecteurs [#474, #466].
- La recherche d'informations se base désormais sur les données locales, améliorant la réactivité de l'application [#473].
- Simplification du processus d'onboarding pour les ETG, collecteurs, SVI et circuits courts, en supprimant l'attente de la page de notifications [#458].
- Possibilité d'exporter les fiches de manière modulaire [#445].
- Redirection automatique des utilisateurs vers le tableau de bord approprié après connexion, évitant les erreurs 404 [#453].
- Affichage du dernier intermédiaire avant l'ETG sur la FEI [#433].
- Ajout d'un filtre "Saison" sur les pages de gestion des fiches [#427].
- Regroupement des carcasses par destinataire pour une meilleure vue d'ensemble pour les chasseurs [#409].
- Gestion du statut "clôturée" d'une FEI via ses carcasses [#414].
- Ajout d'une page listant les utilisateurs ayant interagi avec un ETG [#415].
- Amélioration de l'interface utilisateur et de l'expérience utilisateur pour la création de fiches et les demandes de modifications [#444].
- Amélioration du panel d'administration, notamment l'affichage des villes les plus récentes [#460, #461].
- Affichage de l'entité premier détenteur au lieu de la personne [#442].
- Correction de l'affichage du destinataire choisi par le premier détenteur [#423].

### Évolutions techniques
- Refactorisation de la gestion des transmissions, avec une séparation des étapes et des tests associés [#472, #463].
- Suppression du code legacy lié à Tipimail [#425].
- Amélioration de la gestion du cache lors de la déconnexion [#402].
- Optimisation du chargement des données et de la gestion du statut "en ligne" [#449].
- Mise à jour des scopes des départements pour les utilisateurs [#412, #411].
- Ajout de tests pour la transmission des carcasses depuis l'examinateur initial [#400].
- Activation du cron de relance de complétion de profil.
- Ajout de specs pour la gestion de la trichine [#389].
- Ajout de prettier dans le workflow CI/CD [#393].

### Autres changements
- Nettoyage du code lié à la gestion des carcasses [#464].
- Correction de bugs mineurs et améliorations de la documentation [#457, #459, #456, #452, #451, #450, #443, #440, #437, #434, #432, #431, #430, #429, #428, #426, #424, #422, #421, #420, #417, #416, #413, #410, #403, #401, #399, #398, #397, #396, #395, #392, #391].
- Mise à jour de la documentation pour les emails [#426].
- Amélioration du wording de l'application [#403, #396].
- Ajout d'un tracker pour les erreurs 404 [#420].
- Correction de faux positifs dans les alertes Sentry [#417].
- Ajout d'un bandeau pour le Gamefair [#408].
- Correction de l'affichage du label de la date du jour [#396].
