## Changelog : zacharie (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment au niveau du suivi des carcasses et de la gestion des utilisateurs. Des corrections de bugs et des optimisations ont été apportées pour améliorer la stabilité et la performance de l'application. Des fonctionnalités importantes comme la page dédiée aux carcasses et l'intégration du quiz de prélèvement d'assiette ont été implémentées.

### Évolutions fonctionnelles
- Ajout d'une page dédiée aux carcasses, permettant une visualisation et une gestion plus détaillée. [#353](https://github.com/betagouv/zacharie/issues/353)
- Implémentation du quiz de prélèvement d'assiette pour faciliter la collecte d'informations. [#361](https://github.com/betagouv/zacharie/issues/361)
- Possibilité de grouper les carcasses par destinataire dans la vue chasseur. [#409](https://github.com/betagouv/zacharie/issues/409)
- Amélioration de l'interface utilisateur et de l'expérience utilisateur pour les carcasses. [#373](https://github.com/betagouv/zacharie/issues/373)
- Ajout d'une page 404 personnalisée. [#394](https://github.com/betagouv/zacharie/issues/394)
- Possibilité de modifier le numéro de bracelet ou d'ajouter une carcasse à un examen initial. [#383](https://github.com/betagouv/zacharie/issues/383)
- Amélioration de l'affichage des commentaires des intermédiaires dans la modale. [#358](https://github.com/betagouv/zacharie/issues/358)
- Amélioration des filtres pour les collecteurs. [#357](https://github.com/betagouv/zacharie/issues/357)
- Un chasseur peut voir les destinataires des fiches de son association même s'il n'a pas eu d'interaction avec cette fiche. [#378](https://github.com/betagouv/zacharie/issues/378)
- Suppression du bouton de création de fiche pour un simple chasseur. [#375](https://github.com/betagouv/zacharie/issues/375)
- Correction d'un bug empêchant un utilisateur de changer son rôle. [#416](https://github.com/betagouv/zacharie/issues/416)

### Évolutions techniques
- Refactorisation des contrôleurs pour une meilleure organisation et maintenabilité. [#364](https://github.com/betagouv/zacharie/issues/364), [#368](https://github.com/betagouv/zacharie/issues/368), [#371](https://github.com/betagouv/zacharie/issues/371), [#382](https://github.com/betagouv/zacharie/issues/382)
- Simplification du chargement de Zacharie par les carcasses au lieu des fiches, avec une protection maximale des routes. [#392](https://github.com/betagouv/zacharie/issues/392)
- Ajout de prettier dans le workflow CI/CD. [#393](https://github.com/betagouv/zacharie/issues/393)
- Suppression de code legacy. [#368](https://github.com/betagouv/zacharie/issues/368)
- Amélioration de la gestion du cache lors de la déconnexion. [#402](https://github.com/betagouv/zacharie/issues/402)
- Correction de problèmes de timeout Sentry. [#417](https://github.com/betagouv/zacharie/issues/417)
- Ajout de scripts de démo pour simuler l'activité ETG. [#388](https://github.com/betagouv/zacharie/issues/388)
- Reset correct du store à la déconnexion. [#385](https://github.com/betagouv/zacharie/issues/385)
- Tests de non régression pour préparer le renversement du GET fei vers GET carcasses. [#384](https://github.com/betagouv/zacharie/issues/384)

### Autres changements
- Mise à jour de la portée des départements pour l'utilisateur. [#411](https://github.com/betagouv/zacharie/issues/411), [#412](https://github.com/betagouv/zacharie/issues/412)
- Amélioration du wording pour les carcasses et les lots. [#398](https://github.com/betagouv/zacharie/issues/398)
- Adaptation du responsive des formulaires d'adresse. [#403](https://github.com/betagouv/zacharie/issues/403)
- Amélioration du style du dashboard chasseur. [#401](https://github.com/betagouv/zacharie/issues/401)
- Suppression du téléchargement des utilisateurs des partenaires. [#413](https://github.com/betagouv/zacharie/issues/413)
- Suppression du téléchargement des utilisateurs non concernés. [#410](https://github.com/betagouv/zacharie/issues/410)
- Correction du label du bouton "date du jour". [#396](https://github.com/betagouv/zacharie/issues/396)
- Resserrement de la timeline de transmission. [#397](https://github.com/betagouv/zacharie/issues/397)
- Suppression de vieux liens du backend. [#372](https://github.com/betagouv/zacharie/issues/372)
- Correction de l'invite pour les chasseurs. [#377](https://github.com/betagouv/zacharie/issues/377)
- Activation/désactivation de l'administrateur corrigée. [#376](https://github.com/betagouv/zacharie/issues/376)
- Correction de la configuration des cookies pour les environnements de staging et de production.
