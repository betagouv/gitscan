# Synthèse d'activité : SocialGouv (du 01/11 au 12/11/2026)

## Résumé de l'activité
L'activité récente est marquée par une intégration massive de l'intelligence artificielle, visant à la fois à créer de nouveaux assistants ([stt-form-filler](/repos/SocialGouv/stt-form-filler), [claw-code-go](/repos/SocialGouv/claw-code-go)) et à sécuriser l'usage de ces technologies ([doublure](/repos/SocialGouv/doublure), [smart-allow](/repos/SocialGouv/smart-allow)). Un effort soutenu sur l'accessibilité numérique et la qualité de service est également visible ([egapro](/repos/SocialGouv/egapro), [domifa](/repos/SocialGouv/domifa)).

Parallèlement, l'organisation gère des transitions importantes, incluant la fermeture programmée de certains services ([recosante](/repos/SocialGouv/recosante), [nos1000jours-landing](/repos/SocialGouv/nos1000jours-landing)) et des refontes structurelles de l'infrastructure pour soutenir la croissance ([vao](/repos/SocialGouv/vao), [infra-apps](/repos/SocialGouv/infra-apps)).

## Sécurité
- Protection des données sensibles (PII) lors des échanges avec les modèles d'IA ([doublure](/repos/SocialGouv/doublure)).
- Protection contre l'exfiltration de données vers des fournisseurs d'IA ([smart-allow](/repos/SocialGouv/smart-allow)).
- Corrections de vulnérabilités critiques ([buildkit-operator](/repos/SocialGouv/buildkit-operator), [cdtn-admin](/repos/SocialGouv/cdtn-admin), [archifiltre-mails](/repos/SocialGouv/archifiltre-mails)).
- Renforcement de l'authentification via le support de l'OIDC ([buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example)) et du MFA ([egapro](/repos/SocialGouv/egapro)).
- Anonymisation des données personnelles transmises aux outils de monitoring ([egapro](/repos/SocialGouv/egapro), [srdt](/repos/SocialGouv/srdt)).

## Autres changements notables
- Migrations technologiques majeures : passage à Nuxt v4 ([vao](/repos/SocialGouv/vao)), migration vers PostgreSQL 17 ([egapro](/repos/SocialGouv/egapro)) et mise à jour des environnements Python/Django ([collecte-pro](/repos/SocialGouv/collecte-pro)).
- Évolutions d'infrastructure et d'architecture : déploiement de pools de ressources isolés ([iterion](/repos/SocialGouv/iterion)), adoption de l'architecture "Matryoshka" ([infra-apps](/repos/SocialGouv/infra-apps)) et optimisation de la recherche vectorielle ([questions-ecrites](/repos/SocialGouv/questions-ecrites)).
- Lancement de nouveaux outils de gestion : mise en service du réconciliateur de sources de données Metabase ([metabase-datasource-sync](/repos/SocialGouv/metabase-datasource-sync)) et des outils de migration Harbor ([migration-harbor](/repos/SocialGouv/migration-harbor)).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Avancées majeures sur la gestion des hébergements et migration technique vers Nuxt v4.
- [stt-form-filler](/repos/SocialGouv/stt-form-filler) : Implémentation du remplissage vocal et refonte complète de l'infrastructure de déploiement.
- [iterion](/repos/SocialGouv/iterion) : Évolutions significatives des capacités des agents et renforcement de l'isolation des ressources.
- [egapro](/repos/SocialGouv/egapro) : Mise en conformité majeure avec l'accessibilité et montée en version de la base de données.
- [claw-code-go](/repos/SocialGouv/claw-code-go) : Extension du support des nouveaux modèles d'IA et fiabilisation de l'exécution des commandes.
- [infra-apps](/repos/SocialGouv/infra-apps) : Migration vers la nouvelle architecture d'infrastructure et enrichissement des outils Studio.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Optimisation des performances de recherche vectorielle et de l'ingestion de données.
- [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Intégration de tableaux de bord analytiques et amélioration de la gestion de contenu.
