# Synthèse d'activité : SocialGouv (du 01/09 au 05/11)

## Résumé de l'activité
L'activité de l'organisation est marquée par une accélération majeure sur deux axes : l'intégration sécurisée de l'intelligence artificielle et la modernisation profonde des infrastructures. Les nouveaux outils renforcent la capacité des agents à interagir avec des modèles de pointe tout en garantissant la protection des données sensibles (PII) et la prévention des fuites d'informations.

Parallèlement, une vague de migrations techniques (Nuxt v4, pnpm, Python/Django) et d'optimisations de la résilience des services (bases de données, pools de runners) assure la stabilité et la performance des plateformes. Enfin, l'organisation gère activement le cycle de vie de ses services avec la communication de la fermeture prochaine de plusieurs applications.

## Sécurité
- Protection des données sensibles (PII) et prévention de l'exfiltration de données vers les IA ([smart-allow](/repos/SocialGouv/smart-allow), [doublure](/repos/SocialGouv/doublure)).
- Intégration de scans antivirus systématiques (ClamAV) pour sécuriser les imports de fichiers ([domifa](/repos/SocialGouv/domifa)).
- Durcissement de la sécurité contre les injections, les traversées de chemin et les accès non autorisés ([helmdex](/repos/SocialGouv/helmdex), [egapro](/repos/SocialGouv/egapro), [cdtn-admin](/repos/SocialGouv/cdtn-admin)).
- Correction de vulnérabilités et renforcement de la protection des données ([archifiltre-mails](/repos/SocialGouv/archifiltre-mails), [archifiltre-docs](/repos/SocialGouv/archifiltre-docs)).
- Migration vers des protocoles d'authentification plus robustes comme OIDC ([buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example)).

## Autres changements notables
- **Migrations technologiques majeures** : Passage à Nuxt v4 ([vao](/repos/SocialGouv/vao)), mise à jour de Python/Django ([collecte-pro](/repos/SocialGouv/collecte-pro)) et généralisation de l'outil de gestion de paquets `pnpm` ([matomo-next](/repos/SocialGouv/matomo-next), [revu](/repos/SocialGouv/revu), [jardinmental](/repos/SocialGouv/jardinmental)).
- **Résilience et infrastructure** : Optimisation de la haute disponibilité des bases de données et des systèmes de messagerie, et déploiement de pools de calcul dédiés ([infra-apps](/repos/SocialGouv/infra-apps), [iterion](/repos/SocialGouv/iterion)).
- **Avancées IA** : Support de nouveaux modèles (GPT-6, Opus 5.5) et amélioration des workflows d'agents ([claw-code-go](/repos/SocialGouv/claw-code-go), [iterion](/repos/SocialGouv/iterion)).
- **Optimisation des recherches** : Amélioration des performances de recherche vectorielle ([questions-ecrites](/repos/SocialGouv/questions-ecrites), [srdt](/repos/SocialGouv/srdt)).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Gestion de l'hébergement, création de sites et migrations techniques majeures.
- [infra-apps](/repos/SocialGouv/infra-apps) : Renforcement de la résilience infrastructurelle et évolutions de l'interface Studio.
- [domifa](/repos/SocialGouv/domifa) : Sécurisation des données, intégration antivirus et amélioration de l'expérience de gestion.
- [claw-code-go](/repos/SocialGouv/claw-code-go) : Extension du support des modèles d'IA et fiabilisation de l'exécution des commandes.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Optimisation de la recherche vectorielle et de l'ingestion de données.
- [iterion](/repos/SocialGouv/iterion) : Développement des capacités d'agents et de l'interface Studio.
- [egapro](/repos/SocialGouv/egapro) : Amélioration de la visualisation de données et renforcement de la sécurité.
- [kube-image-keeper](/repos/SocialGouv/kube-image-keeper) : Flexibilité du mirroring d'images et refonte de la documentation.
