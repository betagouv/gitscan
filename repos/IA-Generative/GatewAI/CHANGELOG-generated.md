## Changelog : GatewAI (30 derniers jours, au 09 novembre 2026)

### Résumé
Ce mois a été marqué par une extension significative des capacités de la plateforme, notamment avec l'introduction du support pour le streaming en temps réel via WebSocket. Les performances ont été considérablement optimisées, tant pour le suivi de la consommation que pour la gestion des transferts de fichiers, tout en renforçant la sécurité et la gestion des quotas pour les utilisateurs.

### Évolutions fonctionnelles
- **Support du temps réel** : Introduction d'un proxy de streaming WebSocket incluant le contrôle d'accès lors du handshake, la limitation de la concurrence des sessions et le comptage de la consommation audio.
- **Gestion avancée du débit (Rate-limiting)** : 
    - Ajout de la fonctionnalité `budget_group` permettant de mutualiser les quotas de tokens par modèle.
    - Prise en charge des headers de limitation de débit compatibles avec l'API OpenAI.
    - Amélioration de la précision du calcul du TTL (Time To Live) pour les limites de débit.
- **Gestion des quotas** : Amélioration de la possibilité de réinitialiser les quotas par modèle via l'administration.

### Évolutions techniques
- **Optimisation des performances de reporting** : Refonte du pipeline de reporting d'usage (`GetConsumerUsage`) utilisant des lectures Redis "pipelined". Cela réduit le nombre d'allers-retours réseau de plusieurs milliers à seulement quelques dizaines par requête [#223].
- **Optimisation du streaming de données** : Refactorisation des uploads multipart pour streamer les données directement vers le backend au lieu de les mettre en mémoire tampon, évitant ainsi les fuites de stockage éphémère et l'utilisation excessive de ressources.
- **Mise à jour de l'infrastructure** : Migration vers Go 1.27 et utilisation d'images de base Debian 13 (distroless) pour améliorer la sécurité et la légèreté des conteneurs.
- **Correction de la télémétrie** : Résolution d'un problème de configuration de l'exportateur OTLP qui ne ciblait pas les bons chemins d'accès, rétablissant l'envoi correct des traces et métriques.

### Autres changements
- **Migration de l'organisation** : Transfert complet du projet de `Qatr-io` vers `IA-Generative` (références de code, images Docker, documentation et licence).
- **Documentation** : 
    - Traduction des cartes de fonctionnalités de la page d'accueil en anglais.
    - Ajout de la documentation concernant les headers de rate-limiting et les pools de backends.
    - Mise à jour globale pour corriger les liens morts et les informations obsolètes.
- **Maintenance** : Ajout de labels de source OCI sur les images Docker pour lier les packages GHCR au dépôt.
