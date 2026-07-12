## Changelog : histologe (30 derniers jours, au 10 juillet 2026)

### Résumé
Les dernières mises à jour d'histologe se concentrent sur l'amélioration de l'interconnexion avec les systèmes externes (Esabora, SI Santé Habitat), la correction de bugs et l'amélioration de l'accessibilité de l'application, notamment pour les utilisateurs finaux et les agents. Des améliorations ont également été apportées à la gestion des signalements et des territoires, ainsi qu'à l'interface utilisateur pour les bailleurs.

### Évolutions fonctionnelles
- Amélioration de la reprise des dossiers en erreur lors de la connexion avec Esabora et gestion des doublons. [#6110](https://github.com/MTES-MCT/histologe/issues/6110)
- Envoi de l'adresse complète du bailleur lors de la synchronisation SISH. [#6135](https://github.com/MTES-MCT/histologe/issues/6135)
- Ajout d'un filtre pour les signalements en démarche accélérée dans la liste des signalements en back-office. [#6041](https://github.com/MTES-MCT/histologe/issues/6041)
- Commande temporaire de clôture de signalements en back-office. [#6040](https://github.com/MTES-MCT/histologe/issues/6040) et [#6105](https://github.com/MTES-MCT/histologe/issues/6105)
- Ajout d'une commande pour la clôture massive de signalements à partir d'un fichier CSV. [#5980](https://github.com/MTES-MCT/histologe/issues/5980) et [#6020](https://github.com/MTES-MCT/histologe/issues/6020)
- Amélioration de l'interface de login pour les bailleurs. [#6073](https://github.com/MTES-MCT/histologe/issues/6073)
- Liste des arrêtés disponibles dans la gestion du territoire. [#6026](https://github.com/MTES-MCT/histologe/issues/6026)
- Amélioration des relances dans la démarche accélérée. [#6053](https://github.com/MTES-MCT/histologe/issues/6053)
- Validation de la date d'entrée du logement et reprise des dossiers SCHS pour SI Santé Habitat. [#6090](https://github.com/MTES-MCT/histologe/issues/6090)

### Évolutions techniques
- Adaptation du parser d'étage pour correspondre aux contraintes d'Esabora. [#6100](https://github.com/MTES-MCT/histologe/issues/6100) et [#6106](https://github.com/MTES-MCT/histologe/issues/6106)
- Rationalisation des flush de la base de données (première étape). [#5977](https://github.com/MTES-MCT/histologe/issues/5977)
- Suppression de la variable d'environnement `FEATURE_INJONCTION_BAILLEUR`. [#6000](https://github.com/MTES-MCT/histologe/issues/6000)
- Mise à jour de Jmespath pour corriger une vulnérabilité de sécurité (CVE). [#6028](https://github.com/MTES-MCT/histologe/issues/6028)
- Correction d'une erreur de type lors de la normalisation du code INSEE. [#6055](https://github.com/MTES-MCT/histologe/issues/6055) et [#6062](https://github.com/MTES-MCT/histologe/issues/6062)
- Mise à jour des paquets npm. [#6036](https://github.com/MTES-MCT/histologe/issues/6036) et [#6037](https://github.com/MTES-MCT/histologe/issues/6037)

### Autres changements
- Amélioration de l'accessibilité de l'application :
    - Harmonisation des formulaires. [#5991](https://github.com/MTES-MCT/histologe/issues/5991) et [#6001](https://github.com/MTES-MCT/histologe/issues/6001)
    - Amélioration de la navigation au clavier dans le formulaire Pro. [#6005](https://github.com/MTES-MCT/histologe/issues/6005)
    - Amélioration de l'accessibilité du suivi usager (liens, titres, hiérarchie). [#5993](https://github.com/MTES-MCT/histologe/issues/5993)
    - Modification des champs radio buttons en fieldset pour l'accessibilité. [#5979](https://github.com/MTES-MCT/histologe/issues/5979)
- Corrections diverses HTML dans le front-office (dossier bailleurs). [#6076](https://github.com/MTES-MCT/histologe/issues/6076)
- Amélioration de l'affichage des erreurs de données lors de la connexion avec Esabora. [#6111](https://github.com/MTES-MCT/histologe/issues/6111)
- Correction d'un bug lié à l'export de listes. [#6052](https://github.com/MTES-MCT/histologe/issues/6052)
- Suppression du résumé des suivis généré par l'IA. [#6025](https://github.com/MTES-MCT/histologe/issues/6025) et [#6039](https://github.com/MTES-MCT/histologe/issues/6039)
- Mise à jour des CGU. [#6003](https://github.com/MTES-MCT/histologe/issues/6003)
- Correction de problèmes de pagination dans l'API. [#6075](https://github.com/MTES-MCT/histologe/issues/6075)
- Ajout d'un bandeau d'alerte pour les environnements de test. [#6081](https://github.com/MTES-MCT/histologe/issues/6081)
- Correction de l'accès aux signalements de même adresse (restreint aux admins). [#6035](https://github.com/MTES-MCT/histologe/issues/6035)
- Amélioration de la gestion des erreurs d'envoi d'emails Brevo. [#5952](https://github.com/MTES-MCT/histologe/issues/5952)
- Suppression des dépréciations. [#5962](https://github.com/MTES-MCT/histologe/issues/5962) et [#5982](https://github.com/MTES-MCT/histologe/issues/5982)
