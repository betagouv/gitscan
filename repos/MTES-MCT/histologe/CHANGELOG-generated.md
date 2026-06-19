## Changelog : histologe (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, histologe a bénéficié d'améliorations significatives en termes d'accessibilité, de sécurité et de correction de bugs. Des fonctionnalités ont été ajoutées pour faciliter la gestion des signalements, notamment pour les logements vacants et les doublons d'adresses. Des optimisations techniques ont également été réalisées pour améliorer la performance et la maintenance du code.

### Évolutions fonctionnelles
- **Gestion des signalements :**
    - Restriction de l'accès à la gestion des signalements avec la même adresse aux administrateurs uniquement. [#6035](https://github.com/MTES-MCT/histologe/issues/6035)
    - Ajout d'un message informatif pour les logements vacants lors de l'ajout d'un suivi. [#5897](https://github.com/MTES-MCT/histologe/issues/5897)
    - Enregistrement du nom du travailleur social dans le formulaire de signalement. [#5867](https://github.com/MTES-MCT/histologe/issues/5867)
    - Suppression du blocage du parcours "Parc public" si le bailleur n'est pas prévenu ou l'est trop récemment. [#5854](https://github.com/MTES-MCT/histologe/issues/5854)
- **Interface utilisateur :**
    - Améliorations de l'accessibilité du formulaire de suivi usager, incluant des validations W3C, l'harmonisation des boutons et le déplacement d'un encart. [#5996](https://github.com/MTES-MCT/histologe/issues/5996), [#5991](https://github.com/MTES-MCT/histologe/issues/5991), [#5994](https://github.com/MTES-MCT/histologe/issues/5994)
    - Amélioration de l'accessibilité de la liste des signalements. [#5900](https://github.com/MTES-MCT/histologe/issues/5900)
    - Modification des champs radio buttons en fieldset pour améliorer l'accessibilité du formulaire Pro. [#5979](https://github.com/MTES-MCT/histologe/issues/5979)
- **Fonctionnalités d'administration :**
    - Commande pour mettre à jour les communes fusionnées. [#5910](https://github.com/MTES-MCT/histologe/issues/5910)
    - Commande pour désynchroniser le SISH après 2 jours. [#6019](https://github.com/MTES-MCT/histologe/issues/6024)
    - Commande pour fermer les signalements depuis un fichier CSV. [#5980](https://github.com/MTES-MCT/histologe/issues/6020)
    - Ajout de la colonne "zones" à l'export des signalements. [#5883](https://github.com/MTES-MCT/histologe/issues/5883)
    - Upload des règles pour l'affectation automatique. [#5918](https://github.com/MTES-MCT/histologe/issues/5918)
    - Création d'une liste des doublons de dossiers à la même adresse. [#5864](https://github.com/MTES-MCT/histologe/issues/5981)
- **Autres :**
    - Mise à jour des CGU. [#6003](https://github.com/MTES-MCT/histologe/issues/6003)

### Évolutions techniques
- **Sécurité :**
    - Mise à jour de Jmespath suite à une vulnérabilité (CVE). [#6028](https://github.com/MTES-MCT/histologe/issues/6028)
    - Mise à jour de Twig et Symfony pour corriger des vulnérabilités (CVE). [#5887](https://github.com/MTES-MCT/histologe/issues/5887)
- **Refactoring et Optimisation :**
    - Refactorisation de `JobEventRepository` et `SignalementDraftRepository`. [#5914](https://github.com/MTES-MCT/histologe/issues/5914)
    - Suppression de la variable d'environnement `FEATURE_INJONCTION_BAILLEUR`. [#6000](https://github.com/MTES-MCT/histologe/issues/6000)
    - Suppression ou limitation de l'utilisation des contextes de suivi. [#5884](https://github.com/MTES-MCT/histologe/issues/5884)
    - Suppression d'une route de gestion des images du firewall main. [#5891](https://github.com/MTES-MCT/histologe/issues/5898)
- **Monitoring :**
    - Configuration de Sentry pour ne pas alerter sur les messages provenant du scheduler (queue_name=esabora). [#5978](https://github.com/MTES-MCT/histologe/issues/5978)
- **Déploiement :**
    - Utilisation de `.env.ci` dans l'environnement CI principal. [#5842](https://github.com/MTES-MCT/histologe/issues/5961)

### Autres changements
- Mise à jour de la documentation de l'API. [#5928](https://github.com/MTES-MCT/histologe/issues/5929)
- Mise à jour des paquets npm. [#5965](https://github.com/MTES-MCT/histologe/issues/5965)
- Ajout de types de partenaires. [#5905](https://github.com/MTES-MCT/histologe/issues/5913)
- Correction d'un bug lié au numéro de téléphone lors d'une réunion. [#5957](https://github.com/MTES-MCT/histologe/issues/5957)
- Ajout d'insalubrité en cas d'absence d'eau chaude. [#5908](https://github.com/MTES-MCT/histologe/issues/5947)
- Ajout d'un mini dashboard pour la démarche accélérée. [#5942](https://github.com/MTES-MCT/histologe/issues/5942)
- Correction de l'affichage de l'occupation du logement. [#5909](https://github.com/MTES-MCT/histologe/issues/5909)
- Correction de l'export des utilisateurs non-RT. [#5925](https://github.com/MTES-MCT/histologe/issues/5925)
- Précision des liens et amélioration de la hiérarchie des titres pour l'accessibilité. [#5993](https://github.com/MTES-MCT/histologe/issues/5993)
- Correction de la suppression de la qualification. [#6002](https://github.com/MTES-MCT/histologe/issues/6002)
- Correction d'erreurs et d'avertissements W3C et d'erreurs JS dans le formulaire Pro. [#5975](https://github.com/MTES-MCT/histologe/issues/5975)
- Correction du contrôle du préavis de départ. [#5959](https://github.com/MTES-MCT/histologe/issues/5959)
- Suppression des premières dépréciations. [#5982](https://github.com/MTES-MCT/histologe/issues/5982)
- Correction d'un crash lors de l'ajout d'un utilisateur à un partenaire sans email actif. [#6017](https://github.com/MTES-MCT/histologe/issues/6016)
