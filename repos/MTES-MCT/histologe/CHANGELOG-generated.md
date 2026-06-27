## Changelog : histologe (30 derniers jours, au 26 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'application, notamment en termes d'accessibilité, de gestion des signalements et d'optimisations techniques. Des corrections de bugs et des ajustements ont également été apportés pour améliorer l'expérience utilisateur et la stabilité de la plateforme. L'ajout de nouvelles fonctionnalités facilite le travail des agents de l'administration dans le suivi du mal-logement.

### Évolutions fonctionnelles
- **Gestion des signalements :**
    - Ajout d'un filtre "Démarche accélérée" dans la liste des signalements [#6041](https://github.com/MTES-MCT/histologe/issues/6041).
    - Commande temporaire pour la clôture massive de signalements en back-office [#6040](https://github.com/MTES-MCT/histologe/issues/6040).
    - Possibilité de restreindre l'accès à la gestion des signalements même adresse aux administrateurs [#6035](https://github.com/MTES-MCT/histologe/issues/6035).
    - Ajout de la colonne "zones" à l'export des signalements [#5883](https://github.com/MTES-MCT/histologe/issues/5883).
- **Formulaire et interface utilisateur :**
    - Amélioration de la navigation au clavier dans le formulaire "Pro" [#6005](https://github.com/MTES-MCT/histologe/issues/6005).
    - Corrections d'accessibilité sur le formulaire "Pro" (champs radio, erreurs w3c) [#5979](https://github.com/MTES-MCT/histologe/issues/5979) et [#5975](https://github.com/MTES-MCT/histologe/issues/5975).
    - Harmonisation des boutons d'annulation et d'enregistrement et déplacement de l'encart sur le dossier dans le suivi usager [#5994](https://github.com/MTES-MCT/histologe/issues/5994).
    - Amélioration de l'accessibilité générale (précision des liens, titres et hiérarchie) [#5993](https://github.com/MTES-MCT/histologe/issues/5993).
- **Autres :**
    - Mini dashboard pour la "Démarche Accélérée" [#5942](https://github.com/MTES-MCT/histologe/issues/5942).
    - Mise à jour des CGU [#6003](https://github.com/MTES-MCT/histologe/issues/6003).
    - Suppression du résumé des suivis généré par l'IA [#6025](https://github.com/MTES-MCT/histologe/issues/6025).
    - Ajout de la possibilité de créer une liste des doublons de dossiers (même adresse) [#5864](https://github.com/MTES-MCT/histologe/issues/5864).

### Évolutions techniques
- **Infrastructure et dépendances :**
    - Mise à jour de Jmespath pour corriger une vulnérabilité de sécurité (CVE) [#6028](https://github.com/MTES-MCT/histologe/issues/6028).
    - Mise à jour des dépendances Composer [#5912](https://github.com/MTES-MCT/histologe/issues/5912).
    - Mise à jour des paquets npm [#6036](https://github.com/MTES-MCT/histologe/issues/6036) et [#6043](https://github.com/MTES-MCT/histologe/issues/6043).
    - Mise à jour de TinyMCE [#5955](https://github.com/MTES-MCT/histologe/issues/5955).
- **Architecture et code :**
    - Refactorisation de `JobEventRepository` et `SignalementDraftRepository` [#5914](https://github.com/MTES-MCT/histologe/issues/5914).
    - Rationalisation des flush (première étape) [#5977](https://github.com/MTES-MCT/histologe/issues/5977).
    - Suppression de la variable d'environnement `FEATURE_INJONCTION_BAILLEUR` [#6000](https://github.com/MTES-MCT/histologe/issues/6000).
- **CI/CD et monitoring :**
    - Utilisation de `.env.ci` dans le pipeline CI principal [#5842](https://github.com/MTES-MCT/histologe/issues/5842).
    - Ajout d'un transport dédié pour les messages [#5934](https://github.com/MTES-MCT/histologe/issues/5934).
    - Configuration de Sentry pour ne pas alerter sur les messages provenant du scheduler (queue esabora) [#5978](https://github.com/MTES-MCT/histologe/issues/5978).

### Autres changements
- Documentation de l'API mise à jour [#5928](https://github.com/MTES-MCT/histologe/issues/5928).
- Ajout de types de partenaires [#5905](https://github.com/MTES-MCT/histologe/issues/5905).
- Correction d'un bug lié au numéro de téléphone réunionnais dans le formulaire front-office [#5957](https://github.com/MTES-MCT/histologe/issues/5957).
- Correction d'un bug lié à l'export de la liste [#6052](https://github.com/MTES-MCT/histologe/issues/6052).
- Correction d'un TypeError sur la normalisation du code INSEE [#6055](https://github.com/MTES-MCT/histologe/issues/6055).
- Correction d'un crash lors de l'ajout d'un utilisateur à un partenaire sans email actif [#6016](https://github.com/MTES-MCT/histologe/issues/6016).
- Correction d'une erreur de mail et amélioration du suivi des erreurs d'envoi Brevo [#5952](https://github.com/MTES-MCT/histologe/issues/5952).
- Ajout d'une commande pour désynchroniser Sish après 2 jours [#6019](https://github.com/MTES-MCT/histologe/issues/6019).
- Ajout d'une commande pour fermer les signalements à partir d'un fichier CSV [#5980](https://github.com/MTES-MCT/histologe/issues/5980).
- Correction d'un problème de qualification [#6002](https://github.com/MTES-MCT/histologe/issues/6002).
- Ajout de la prise en charge de l'absence d'eau chaude comme insalubrité [#5908](https://github.com/MTES-MCT/histologe/issues/5908).
- Correction de la synchronisation des erreurs messenger doctrine [#5921](https://github.com/MTES-MCT/histologe/issues/5921).
- Autorisation des scripts Matomo depuis stats.beta.gouv.fr [#5938](https://github.com/MTES-MCT/histologe/issues/5938).
