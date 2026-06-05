## Changelog : zacharie (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Zacharie en se concentrant sur l'expérience utilisateur, notamment au niveau de la gestion des carcasses, des fiches et des utilisateurs. Des corrections de bugs et des améliorations de la sécurité ont également été apportées. Des fonctionnalités importantes comme le filtre par saison et la gestion du statut "clôturée" des FEIs ont été implémentées.

### Évolutions fonctionnelles
- Ajout d'un filtre "Saison" (1er juin - 31 mai) sur les pages fiches, facilitant la recherche et l'organisation des données. [#427](https://github.com/betagouv/zacharie/issues/427)
- Affichage des sous-totaux de carcasses par espèce pour une meilleure analyse des données. [#424](https://github.com/betagouv/zacharie/issues/424)
- Gestion du statut "cloturée" d'une FEI via ses carcasses, permettant un suivi plus précis du cycle de vie des données. [#414](https://github.com/betagouv/zacharie/issues/414)
- Ajout d'une page listant les utilisateurs ayant interagi avec l'ETG, facilitant la gestion des accès et des permissions. [#415](https://github.com/betagouv/zacharie/issues/415)
- Amélioration de l'affichage du destinataire choisi par le premier détenteur. [#423](https://github.com/betagouv/zacharie/issues/423)
- Ajout d'un bouton permettant aux administrateurs de supprimer des utilisateurs. [#429](https://github.com/betagouv/zacharie/issues/429)
- Regroupement des carcasses par destinataire dans la vue chasseur pour une meilleure organisation. [#409](https://github.com/betagouv/zacharie/issues/409)
- Possibilité de modifier le numéro de bracelet ou d'ajouter une carcasse à un examen initial. [#383](https://github.com/betagouv/zacharie/issues/383)
- Nouvelle page dédiée aux carcasses (#353)
- Ajout d'un quiz pour le prélèvement et l'assiette. [#361](https://github.com/betagouv/zacharie/issues/361)
- Amélioration de l'interface utilisateur et de l'expérience utilisateur pour les carcasses. [#373](https://github.com/betagouv/zacharie/issues/373)

### Évolutions techniques
- Refonte de la gestion des scopes des départements utilisateurs. [#412](https://github.com/betagouv/zacharie/issues/412) et [#411](https://github.com/betagouv/zacharie/issues/411)
- Simplification des contrôleurs utilisateurs et des fonctions de synchronisation. [#364](https://github.com/betagouv/zacharie/issues/364) et [#371](https://github.com/betagouv/zacharie/issues/371)
- Suppression de code legacy et de contrôleurs obsolètes. [#368](https://github.com/betagouv/zacharie/issues/368), [#369](https://github.com/betagouv/zacharie/issues/369) et [#372](https://github.com/betagouv/zacharie/issues/372)
- Amélioration du chargement de Zacharie via les carcasses plutôt que les fiches pour une meilleure performance et sécurité. [#392](https://github.com/betagouv/zacharie/issues/392)
- Ajout de prettier dans le workflow CI/CD pour garantir la cohérence du code. [#393](https://github.com/betagouv/zacharie/issues/393)
- Activation du cron de relance de complétion de profil.
- Ajout de specs pour les trichines. [#389](https://github.com/betagouv/zacharie/issues/389)
- Ajout d'un tracker sur les pages 404 pour l'analyse du trafic.
- Suppression du code legacy tipimail. [#425](https://github.com/betagouv/zacharie/issues/425)

### Autres changements
- Changement de logo pour une meilleure lisibilité. [#431](https://github.com/betagouv/zacharie/issues/431)
- Amélioration du design des pages de détails administrateur. [#430](https://github.com/betagouv/zacharie/issues/430)
- Correction de bugs concernant l'onboarding, la gestion des rôles utilisateurs, et l'affichage des informations. [#422](https://github.com/betagouv/zacharie/issues/422), [#416](https://github.com/betagouv/zacharie/issues/416), [#428](https://github.com/betagouv/zacharie/issues/428)
- Correction de problèmes liés à l'affichage des commentaires des intermédiaires et des filtres collecteurs. [#358](https://github.com/betagouv/zacharie/issues/358), [#357](https://github.com/betagouv/zacharie/issues/357)
- Ajout d'un bandeau pour le Gamefair.
- Ajout d'un redirect pour les pages 404.
- Amélioration du wording des carcasses et des lots. [#398](https://github.com/betagouv/zacharie/issues/398)
- Adaptation du responsive des formulaires d'adresse. [#403](https://github.com/betagouv/zacharie/issues/403)
- Amélioration du style du dashboard chasseur. [#401](https://github.com/betagouv/zacharie/issues/401)
- Correction de problèmes de cache lors de la déconnexion et du changement d'utilisateur. [#402](https://github.com/betagouv/zacharie/issues/402) et [#378](https://github.com/betagouv/zacharie/issues/378)
- Suppression des invitations pour les chasseurs. [#377](https://github.com/betagouv/zacharie/issues/377)
- Correction du toggle admin. [#376](https://github.com/betagouv/zacharie/issues/376)
- Correction d'un bug empêchant un utilisateur de changer son rôle. [#416](https://github.com/betagouv/zacharie/issues/416)
- Correction d'un problème de gestion des comptes non examinateurs. [#432](https://github.com/betagouv/zacharie/issues/432)
