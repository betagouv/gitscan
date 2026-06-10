## Changelog : zacharie (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Zacharie avec un focus sur la gestion des carcasses, l'expérience utilisateur et la correction de bugs. Des améliorations significatives ont été apportées à la gestion des rôles utilisateurs, à l'onboarding et à la traçabilité du gibier. De nouvelles fonctionnalités, comme la page carcasse et le quiz sur le prélèvement d'assiette, ont été ajoutées.

### Évolutions fonctionnelles
- Ajout d'une page dédiée à la gestion des carcasses, permettant une vue détaillée et des actions spécifiques sur chaque carcasse [#353](https://github.com/betagouv/zacharie/issues/353).
- Implémentation d'un filtre "Saison" sur les pages de fiches, facilitant la recherche et l'organisation des données [#427](https://github.com/betagouv/zacharie/issues/427).
- Possibilité pour un administrateur de supprimer un utilisateur via une nouvelle fonctionnalité dans l'interface d'administration [#429](https://github.com/betagouv/zacharie/issues/429).
- Amélioration de l'affichage des sous-totaux de carcasses par espèce [#424](https://github.com/betagouv/zacharie/issues/424).
- Ajout d'un quiz sur le prélèvement d'assiette [#361](https://github.com/betagouv/zacharie/issues/361).
- Gestion du statut "clôturée" d'une FEI (Fiche d'Examen Initial) via ses carcasses [#414](https://github.com/betagouv/zacharie/issues/414).
- Page listant les utilisateurs ayant interagi avec une ETG (Épreuve Technique de Gestion) [#415](https://github.com/betagouv/zacharie/issues/415).
- Amélioration de l'interface utilisateur pour les carcasses [#373](https://github.com/betagouv/zacharie/issues/373).
- Correction de l'affichage du destinataire choisi par le premier détenteur [#423](https://github.com/betagouv/zacharie/issues/423).
- Amélioration de l'expérience utilisateur pour la création d'associations de chasse [#380](https://github.com/betagouv/zacharie/issues/380).
- Gestion des erreurs et amélioration des messages d'erreur [#365](https://github.com/betagouv/zacharie/issues/365).

### Évolutions techniques
- Refactorisation des contrôleurs pour une meilleure organisation et maintenabilité [#364](https://github.com/betagouv/zacharie/issues/364), [#369](https://github.com/betagouv/zacharie/issues/369), [#371](https://github.com/betagouv/zacharie/issues/371).
- Simplification de la gestion des utilisateurs et des permissions.
- Amélioration de la gestion du cache pour une meilleure performance et une meilleure expérience utilisateur [#402](https://github.com/betagouv/zacharie/issues/402).
- Suppression de code legacy et de dépendances inutiles.
- Ajout de tests pour la transmission des carcasses depuis un examinateur initial [#400](https://github.com/betagouv/zacharie/issues/400).
- Ajout de prettier dans le workflow CI/CD pour assurer la cohérence du code [#393](https://github.com/betagouv/zacharie/issues/393).
- Amélioration de la synchronisation des données et des routes API.
- Mise à jour des scopes utilisateurs pour une meilleure gestion des accès.

### Autres changements
- Ajout de documentation pour les emails.
- Mise à jour du fichier `claude.md`.
- Ajout d'un tracker pour les pages 404 afin de mieux comprendre les erreurs de navigation [#420](https://github.com/betagouv/zacharie/issues/420).
- Ajout d'un script de démo pour simuler l'activité ETG [#388](https://github.com/betagouv/zacharie/issues/388).
- Correction de faux positifs dans les alertes Sentry.
- Amélioration du bandeau pour le Gamefair.
- Changement de logo pour une meilleure lisibilité [#431](https://github.com/betagouv/zacharie/issues/431).
- Correction du design des pages de détails administrateur [#430](https://github.com/betagouv/zacharie/issues/430).
- Activation du cron de relance de complétion de profil.
- Correction d'un bug empêchant un utilisateur de changer son rôle [#416](https://github.com/betagouv/zacharie/issues/416).
- Correction d'un bug lié à l'onboarding et à la formation obligatoire [#422](https://github.com/betagouv/zacharie/issues/422).
- Correction d'un bug empêchant les non-examinateurs d'accéder à certaines fonctionnalités [#432](https://github.com/betagouv/zacharie/issues/432).
- Correction d'un bug lié à l'envoi de mails d'onboarding [#428](https://github.com/betagouv/zacharie/issues/428).
