## Changelog : fondation (30 derniers jours, au 09/10/2026)

### Résumé
Ce mois-ci, l'outil a franchi une étape importante dans la gestion des sessions et des auditions, tout en renforçant l'interaction avec les utilisateurs grâce à un nouveau système de feedback. L'interface a été fluidifiée pour faciliter la navigation et la fiabilité technique a été consolidée par des refactorisations et des correctifs de sécurité.

### Évolutions fonctionnelles
- **Auditions et sessions** : possibilité de lister et planifier les auditions d'une session [#679](https://github.com/betagouv/fondation/issues/679) et de publier la table des auditions aux membres [#687](https://github.com/betagouv/fondation/issues/687).
- **Feedback et satisfaction** : mise en place de l'option "Je donne mon avis" [#644](https://github.com/betagouv/fondation/issues/644), de questionnaires de satisfaction par session [#681](https://github.com/betagouv/fondation/issues/681) et d'un suivi global des réponses [#686](https://github.com/betagouv/fondation/issues/686).
- **Profils et données magistrats** : amélioration de l'affichage des informations (nom de jeune fille, prénom, numéros de téléphone) [#691](https://github.com/betagouv/fondation/issues/691) [#682](https://github.com/betagouv/fondation/issues/682).
- **Gestion documentaire** : les documents restent en mode brouillon jusqu'à leur validation [#657](https://github.com/betagouv/fondation/issues/657) et les blocs de texte acceptent désormais les sauts de ligne [#671](https://github.com/betagouv/fondation/issues/671).
- **Notifications** : les alertes sont désormais envoyées via Tchap au lieu de Mattermost [#689](https://github.com/betagouv/fondation/issues/689).
- **Interface et accessibilité** : amélioration de la visibilité avec une barre de session épinglée [#649](https://github.com/betagouv/fondation/issues/649) [#651](https://github.com/betagouv/fondation/issues/651), ajout d'une page de déclaration d'accessibilité [#630](https://github.com/betagouv/fondation/issues/630) et navigation simplifiée entre les rapports des membres [#647](https://github.com/betagouv/fondation/issues/647).
- **Corrections diverses** : ajustements sur le statut des fichiers [#696](https://github.com/betagouv/fondation/issues/696), la gestion des rapports officiels [#670](https://github.com/betagouv/fondation/issues/670) [#627](https://github.com/betagouv/fondation/issues/627) et la clarté des messages d'alerte [#699](https://github.com/betagouv/fondation/issues/699).

### Évolutions techniques
- **Architecture et code** : refactorisation pour supprimer les cycles d'importation entre les modules membres et magistrats [#695](https://github.com/betagouv/fondation/issues/695) et généralisation de l'utilisation des services pour la communication entre modules [#692](https://github.com/betagouv/fondation/issues/692).
- **Tests et monitoring** : ajout de la mesure de couverture pour les suites de tests unitaires et E2E [#628](https://github.com/betagouv/fondation/issues/628) et intégration du suivi analytique Matomo [#635](https://github.com/betagouv/fondation/issues/635).
- **Sécurité et maintenance** : correction de vulnérabilités sur les dépendances `multer` et `qs` [#673](https://github.com/betagouv/fondation/issues/673) et optimisation de la suppression des fichiers après la validation des transactions [#659](https://github.com/betagouv/fondation/issues/659).
- **Fiabilité des données** : renforcement de la vérification des champs via Prisma [#660](https://github.com/betagouv/fondation/issues/660).

### Autres changements
- **Documentation** : mise à jour des instructions concernant l'importation des données LOLFI et les chemins d'archives [#684](https://github.com/betagouv/fondation/issues/684).
- **Données de test** : peuplement des environnements locaux et de staging avec des données LOLFI fictives pour faciliter les tests [#683](https://github.com/betagouv/fondation/issues/683).
