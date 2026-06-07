## Changelog : zacharie (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Zacharie avec un focus sur la gestion des carcasses, l'expérience utilisateur et la correction de bugs. Des améliorations ont été apportées à l'interface pour faciliter la navigation et la gestion des données, notamment pour les chasseurs et les administrateurs. Des fonctionnalités liées à la traçabilité de la trichine et à la gestion des examens initiaux ont également été implémentées.

### Évolutions fonctionnelles
- Ajout d'une page dédiée à la gestion des carcasses, permettant une vue détaillée et des actions spécifiques. [#353](https://github.com/betagouv/zacharie/issues/353)
- Possibilité de grouper les carcasses par destinataire pour les chasseurs, améliorant l'organisation et la visualisation des données. [#409](https://github.com/betagouv/zacharie/issues/409)
- Ajout d'un filtre "Saison" sur les pages de fiches, facilitant la recherche et le tri des données. [#427](https://github.com/betagouv/zacharie/issues/427)
- Implémentation de la gestion du statut "clôturée" pour les FEIs (Fiches d'Examen Initial) via leurs carcasses. [#414](https://github.com/betagouv/zacharie/issues/414)
- Ajout d'une page listant les utilisateurs ayant interagi avec l'ETG (Établissement Technique de Génétique). [#415](https://github.com/betagouv/zacharie/issues/415)
- Amélioration de l'interface utilisateur pour les carcasses, rendant la gestion plus intuitive. [#373](https://github.com/betagouv/zacharie/issues/373)
- Ajout d'un bouton pour supprimer un utilisateur depuis l'interface administrateur. [#429](https://github.com/betagouv/zacharie/issues/429)
- Possibilité de modifier le numéro de bracelet ou d'ajouter une carcasse à un examen initial. [#383](https://github.com/betagouv/zacharie/issues/383)
- Ajout d'un quiz pour le prélèvement d'assiette. [#361](https://github.com/betagouv/zacharie/issues/361)
- Ajout d'une page 404 personnalisée. [#394](https://github.com/betagouv/zacharie/issues/394)

### Évolutions techniques
- Refactorisation et simplification des contrôleurs pour améliorer la maintenabilité du code. [#364](https://github.com/betagouv/zacharie/issues/364), [#369](https://github.com/betagouv/zacharie/issues/369), [#382](https://github.com/betagouv/zacharie/issues/382)
- Amélioration de la gestion du cache pour une meilleure performance et une expérience utilisateur plus fluide. [#402](https://github.com/betagouv/zacharie/issues/402)
- Suppression de code legacy et de fonctions de synchronisation obsolètes. [#371](https://github.com/betagouv/zacharie/issues/371), [#368](https://github.com/betagouv/zacharie/issues/368)
- Ajout de tests pour la transmission des carcasses depuis un examinateur initial. [#400](https://github.com/betagouv/zacharie/issues/400)
- Ajout de prettier dans le workflow CI/CD pour assurer la cohérence du code. [#393](https://github.com/betagouv/zacharie/issues/393)
- Activation du cron de relance de complétion de profil.
- Modification du scope des départements pour les utilisateurs. [#412](https://github.com/betagouv/zacharie/issues/412), [#411](https://github.com/betagouv/zacharie/issues/411)

### Autres changements
- Mise à jour de la documentation pour les emails.
- Mise à jour du fichier claude.md.
- Correction de bugs concernant l'onboarding, notamment le choix de la formation à l'examen initial. [#422](https://github.com/betagouv/zacharie/issues/422)
- Correction de bugs liés à l'affichage des destinataires des fiches et à l'accès aux fonctionnalités pour les différents rôles utilisateurs. [#423](https://github.com/betagouv/zacharie/issues/423), [#416](https://github.com/betagouv/zacharie/issues/416), [#378](https://github.com/betagouv/zacharie/issues/378), [#375](https://github.com/betagouv/zacharie/issues/375)
- Correction de bugs d'affichage et de style sur différentes pages. [#430](https://github.com/betagouv/zacharie/issues/430), [#403](https://github.com/betagouv/zacharie/issues/403), [#401](https://github.com/betagouv/zacharie/issues/401)
- Ajout d'un tracker sur les pages 404.
- Suppression de code legacy lié à Tipimail. [#425](https://github.com/betagouv/zacharie/issues/425)
- Ajout de specs pour la trichine. [#389](https://github.com/betagouv/zacharie/issues/389)
- Correction de problèmes liés au bandeau Gamefair.
- Amélioration des messages d'erreur. [#365](https://github.com/betagouv/zacharie/issues/365)
- Correction de faux positifs Sentry. [#417](https://github.com/betagouv/zacharie/issues/417)
- Suppression du téléchargement des utilisateurs des partenaires. [#413](https://github.com/betagouv/zacharie/issues/413) et [#410](https://github.com/betagouv/zacharie/issues/410)
