## Changelog : trackdechets (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des déchets, notamment avec l'implémentation de nouvelles fonctionnalités pour le BSFF (Bon de Suivi des Flux de Déchets) et le BSDD (Bon de Suivi des Déchets Dangereux). Des corrections et des améliorations ont également été apportées à l'interface utilisateur et à la sécurité de la plateforme, avec l'ajout de l'authentification à double facteur.

### Évolutions fonctionnelles
- **BSFF :**
    - Implémentation de l'intégration BSFF au DSFR (Dépôt Simple et Sécurisé des Flux de Déchets) avec l'ajout des champs émetteur, transporteur et destination. [#4743](https://github.com/MTES-MCT/trackdechets/issues/4743)
    - Correction d'un bug empêchant la saisie ou la modification des informations de contact de l'installation TTR du regroupement. [#4767](https://github.com/MTES-MCT/trackdechets/issues/4767) et [#4750](https://github.com/MTES-MCT/trackdechets/issues/4750)
    - Ajout d'un tableau pour la gestion des détenteurs dans le BSFF.
    - Implémentation des règles BSFF.
- **BSDD :**
    - Possibilité de modifier les intermédiaires sur un BSDD jusqu'à la signature de la réception par la destination (étape 1 et 2). [#4741](https://github.com/MTES-MCT/trackdechets/issues/4741) et [#4738](https://github.com/MTES-MCT/trackdechets/issues/4738)
    - Possibilité d'ajouter deux intermédiaires supplémentaires sur un BSDD.
- **Authentification :**
    - Ajout de l'authentification à double facteur (2FA) avec activation et désactivation. [#4739](https://github.com/MTES-MCT/trackdechets/issues/4739), [#4740](https://github.com/MTES-MCT/trackdechets/issues/4740) et [#4736](https://github.com/MTES-MCT/trackdechets/issues/4736)
- **Codes déchets :**
    - Création d'une liste de Codes déchets Bâle sur le même principe que la liste des codes déchets. [#4737](https://github.com/MTES-MCT/trackdechets/issues/4737)
- **Registre :**
    - Permettre à un établissement ayant le profil "Installation de valorisation de terres et sédiments" d’accéder à l’export du registre réglementaire entrant et sortant. [#4748](https://github.com/MTES-MCT/trackdechets/issues/4748)

### Évolutions techniques
- Préparation de la recette du 28 avril 2026. [#4742](https://github.com/MTES-MCT/trackdechets/issues/4742)
- Corrections de conditions de verrouillage des champs selon les cas d'utilisation. [#4751](https://github.com/MTES-MCT/trackdechets/issues/4751)
- Correction de l'espacement entre les colonnes.
- Suppression de code inutile et nettoyage de l'interface utilisateur pour la recette.
- Ajout d'un script pour la modification de la base de données. [#4744](https://github.com/MTES-MCT/trackdechets/issues/4744)

### Autres changements
- Mise à jour de la description du footer.
- Correction de problèmes d'affichage de CRISP pour la policy. [#4745](https://github.com/MTES-MCT/trackdechets/issues/4745)
- Modification du nom Géorisque par Trackdéchet. [#4749](https://github.com/MTES-MCT/trackdechets/issues/4749) et [#4759](https://github.com/MTES-MCT/trackdechets/issues/4759)
- Correction de l'espacement entre les colonnes.
- Suppression de code inutile.
- Correction de l'espacement entre les colonnes.
- Rebase depuis une ancienne branche fork.
- Correction d'un problème de pull request concernant la génération de nombres aléatoires.
- Correction de la découpe de la liste des codes bales.
