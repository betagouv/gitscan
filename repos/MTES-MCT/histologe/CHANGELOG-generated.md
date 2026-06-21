## Changelog : histologe (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, histologe a bénéficié d'améliorations significatives en termes d'accessibilité, de correction de bugs et d'optimisations techniques. Des fonctionnalités ont été ajoutées pour faciliter la gestion des signalements, notamment pour les logements vacants et l'enregistrement des informations sur les travailleurs sociaux. L'interface utilisateur a été améliorée pour une meilleure expérience, en particulier pour les agents de l'administration.

### Évolutions fonctionnelles
- **Suivi Usager (FO) :** Amélioration de l'accessibilité avec des validations W3C, harmonisation des formulaires et amélioration de la hiérarchie des titres et des liens. [#5996] [#5991] [#5994] [#5993]
- **Signalements :**
    - Ajout d'un message informatif pour les logements vacants lors de l'ajout d'un suivi. [#5897]
    - Enregistrement du nom du travailleur social dans le formulaire de signalement. [#5867]
    - Ajout de la colonne "zones" dans l'export des signalements. [#5883]
    - Possibilité d'ajouter l'insalubrité en cas d'absence d'eau chaude. [#5908]
- **Annuaire (BO) :** Correction de l'export pour les utilisateurs non-RT. [#5925]
- **Affectation Automatique (BO) :** Possibilité d'uploader des règles pour l'affectation automatique. [#5918]
- **Liste des Signalements (BO) :** Les étiquettes et partenaires sont maintenant triés alphabétiquement, sans tenir compte de la casse. [#5916]
- **RT (BO) :** Création d'une liste des doublons de dossiers à la même adresse. [#5864]
- **Dashboard (BO) :** Invalidation du cache pour éviter les problèmes d'affichage. [#5902]
- **Démarche Accélérée :** Ajout d'un mini dashboard pour une vue d'ensemble. [#5942]
- **Formulaire Pro (BO) :** Amélioration de l'accessibilité avec la modification des champs radio et correction des erreurs W3C et JS. [#5979] [#5975]
- **Restriction d'accès (BO) :** Restriction de l'accès à la fonctionnalité "Signalements même adresse" aux administrateurs uniquement. [#6035]

### Évolutions techniques
- **Sécurité :** Mise à jour de la librairie Jmespath suite à une CVE détectée. [#6028]
- **Refactoring :** Refactorisation des classes `JobEventRepository` et `SignalementDraftRepository`. [#5914]
- **Dépendances :** Mise à jour des dépendances Composer et NPM. [#5912] [#6037]
- **Sentry :** Configuration pour ne pas alerter sur les messages provenant du scheduler Esabora. [#5978]
- **Environnement :** Utilisation du fichier `.env.ci` pour les tests en CI. [#5842]
- **Suppression de code obsolète :** Suppression de la variable d'environnement `FEATURE_INJONCTION_BAILLEUR`. [#6000]
- **Commandes :** Ajout d'une commande pour désynchroniser Sish après 2 jours. [#6019] et d'une commande pour fermer des signalements à partir d'un fichier CSV [#6020]
- **Correction de dépréciations :** Correction des premières dépréciations. [#5962]

### Autres changements
- **Documentation :** Mise à jour de la documentation de l'API. [#5928]
- **Communes :** Ajout d'une commande pour mettre à jour les communes fusionnées. [#5910]
- **Types de partenaires :** Ajout de types de partenaires. [#5905]
- **Qualifiaction :** Correction d'un bug lié à la suppression des qualifications. [#6002]
- **Configuration :** Mise à jour des CGU. [#6003]
- **Messagerie Espace Bailleur :** Modification du champ d'upload de fichier. [#5940]
- **Correction d'un bug :** Correction d'un crash lors de l'ajout d'un utilisateur partenaire sans email actif. [#6017]
- **Correction d'un bug :** Correction d'un bug lié à l'affichage du numéro de téléphone réunionnais. [#5957]
