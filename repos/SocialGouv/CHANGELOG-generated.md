# Synthèse d'activité : SocialGouv (du 15/09 au 22/10)

## Résumé de l'activité
L'activité récente est marquée par une intégration poussée de l'intelligence artificielle, notamment pour l'analyse de code ([repo-falcon](/repos/SocialGouv/repo-falcon)), la protection des données ([doublure](/repos/SocialGouv/doublure)) et l'amélioration de l'accessibilité ([dsfr-mcp](/repos/SocialGouv/dsfr-mcp)). Les outils de services publics se modernisent avec l'ajout de nouveaux simulateurs ([code-du-travail-numerique](/repos/SocialGouv/code-du-travail-numerique)) et une recherche juridique plus précise ([srdt](/repos/SocialGouv/srdt)).

Parallèlement, l'organisation gère la transition de plusieurs services vers leur fermeture ([recosante](/repos/SocialGouv/recosante), [nos1000jours-landing](/repos/SocialGouv/nos1000jours-landing)) tout en consolidant ses infrastructures de déploiement et de gestion de données ([mesure-impact](/repos/SocialGouv/mesure-impact), [iterion](/repos/SocialGouv/iterion)).

## Sécurité
- **Protection des données et confidentialité** : Mise en place de protections automatisées des données sensibles (PII) lors des échanges avec les IA ([doublure](/repos/SocialGouv/doublure)) et prévention de l'exfiltration de données vers des fournisseurs d'IA ([smart-allow](/repos/SocialGouv/smart-allow)).
- **Renforcement de l'authentification** : Migration vers une authentification basée sur OIDC ([buildkit-operator](/repos/SocialGouv/buildkit-operator), [da-manager](/repos/SocialGouv/da-manager), [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example)) et amélioration de la gestion de l'expiration des mots de passe ([domifa](/repos/SocialGouv/domifa)).
- **Durcissement applicatif** : Renforcement de la sécurité contre les injections et le path traversal ([helmdex](/repos/SocialGouv/helmdex)), et mise en conformité avec des politiques de sécurité renforcées (CSP, CSRF, 2FA) ([egapro](/repos/SocialGouv/egapro)).
- **Corrections de vulnérabilités** : Résolution de failles de sécurité identifiées ([archifiltre-mails](/repos/SocialGouv/archifiltre-mails), [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget)).

## Autres changements notables
- **Migrations technologiques majeures** : Passage à Nuxt v4 ([vao](/repos/SocialGouv/vao)), adoption massive du gestionnaire de paquets `pnpm` ([jardinmental](/repos/SocialGouv/jardinmental), [matomo-next](/repos/SocialGouv/matomo-next), [revu](/repos/SocialGouv/revu)), et migration de composants critiques vers le langage Go ([smart-allow](/repos/SocialGouv/smart-allow), [helmdex](/repos/SocialGouv/helmdex)).
- **Évolutions d'infrastructure et de données** : Migration du stockage d'objets vers SeaweedFS ([infra-apps](/repos/SocialGouv/infra-apps)), optimisation des moteurs de recherche vectorielle ([questions-ecrites](/repos/SocialGouv/questions-ecrites)) et mise à jour des bases de données ([egapro](/repos/SocialGouv/egapro)).
- **Avancées en Intelligence Artificielle** : Introduction du routage adaptatif pour les politiques LLM ([iterion](/repos/SocialGouv/iterion)) et extension du support des nouveaux modèles d'IA ([claw-code-go](/repos/SocialGouv/claw-code-go)).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Évolutions sur la gestion de l'hébergement et migration vers Nuxt v4.
- [iterion](/repos/SocialGouv/iterion) : Avancées sur le routage IA, l'isolation des ressources et le monitoring.
- [claw-code-go](/repos/SocialGouv/claw-code-go) : Support étendu des nouveaux modèles d'IA et fiabilisation des commandes.
- [domifa](/repos/SocialGouv/domifa) : Refonte de l'interface utilisateur et renforcement de la sécurité.
- [egapro](/repos/SocialGouv/egapro) : Améliorations majeures de l'accessibilité (RGAA) et de la sécurité.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Optimisation des performances de recherche vectorielle.
- [infra-apps](/repos/SocialGouv/infra-apps) : Stabilisation de l'infrastructure et nouveaux outils de revue de code.
