# Synthèse d'activité : proconnect-gouv (du 28 avril 2026 au 07 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de la stabilité, de la sécurité et des fonctionnalités de ses différents services. Plusieurs dépôts ont bénéficié de mises à jour pour supporter de nouveaux standards d'authentification (eIDAS), améliorer la gestion des erreurs et des logs, et enrichir les données disponibles (informations sur les établissements publics, rôles utilisateurs). Des efforts importants ont également été déployés pour améliorer l'expérience utilisateur, notamment avec l'ajout d'un mode sombre et des corrections d'interface. Les dépôts [proconnect-identite](/repos/proconnect-gouv/proconnect-identite), [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) et [federation](/repos/proconnect-gouv/federation) ont été particulièrement actifs.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour de dépendances pour corriger des vulnérabilités et renforcer la sécurité. Notamment, le dépôt [class-validator](/repos/proconnect-gouv/class-validator) a corrigé des failles de sécurité dans ses dépendances. Le dépôt [federation](/repos/proconnect-gouv/federation) a également renforcé la sécurité en utilisant HTTPS pour récupérer le core-fca.

## Autres changements notables
- Le dépôt [idp-status-monitoring](/repos/proconnect-gouv/idp-status-monitoring) a implémenté un système de healthchecks pour améliorer la robustesse du monitoring.
- Le dépôt [class-validator](/repos/proconnect-gouv/class-validator) a vu l'ajout de nouveaux validateurs pour les formats IBAN, ISO 639-1, ISO 3166-1 et UUID, offrant une validation plus complète des données.
- Le dépôt [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) a corrigé une fuite mémoire et est revenu à l'utilisation d'Axios pour les requêtes HTTP, améliorant ainsi sa stabilité.

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de la stabilité, ajout d'informations sur la taille des établissements publics et implémentation de points de terminaison de ping.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Ajout d'un mode maintenance et amélioration de la documentation pour l'authentification et la gestion des erreurs.
- [federation](/repos/proconnect-gouv/federation) : Amélioration des messages d'erreur, ajout d'un indicateur de maintenance, implémentation de healthchecks et renforcement de la sécurité.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Ajout du mode sombre et corrections d'interface utilisateur.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et correction de vulnérabilités de dépendances.
