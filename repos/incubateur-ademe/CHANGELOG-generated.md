# Synthèse d'activité : incubateur-ademe (du 01/08 au 07/08)

## Résumé de l'activité
L'activité récente de l'organisation se caractérise par une double dynamique : l'amélioration continue de l'expérience utilisateur et la modernisation profonde des socles techniques. Les utilisateurs bénéficient de refontes ergonomiques majeures sur plusieurs outils de comparaison et de gestion de projets, ainsi que de l'intégration de nouvelles fonctionnalités comme l'intelligence artificielle pour les notifications ou des modes de déclaration simplifiés.

En parallèle, l'organisation investit massivement dans la fiabilité et la sécurité, avec des mises à jour cruciales des modèles de calcul d'empreinte carbone et des corrections de vulnérabilités. Ces efforts s'accompagnent de migrations technologiques importantes visant à pérenniser les services, à améliorer la performance et à optimiser les processus de déploiement.

## Sécurité
- Correction de vulnérabilités critiques (IDOR et injections CSV) garantissant l'étanchéité des données entre les collectivités ([territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions)).
- Résolution de failles d'autorisation et de fuites de données ([nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app)).
- Renforcement de l'authentification via l'intégration du SSO OAuth et de la 2FA ([roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles)), la migration vers l'authentification FGP ([grafana](/repos/incubateur-ademe/grafana)) et l'amélioration de la gestion du 2FA ([vaultwarden](/repos/incubateur-ademe/vaultwarden)).
- Mise en place du chiffrement des données sensibles ([tacct-legacy-nextjs](/repos/incubateur-ademe/tacct-legacy-nextjs)).

## Autres changements notables
- Migrations majeures d'infrastructure et de gestion de contenu, notamment vers Wagtail ([plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail)) et vers Scalingo ([metabase](/repos/incubateur-ademe/metabase)).
- Refonte architecturale et passage à TypeScript pour améliorer la maintenabilité et la robustesse ([dsfr-override](/repos/incubateur-ademe/dsfr-override), [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy)).
- Optimisation des processus de déploiement, notamment pour les monorepos pnpm ([ngc-scalingo-buildpack](/repos/incubateur-ademe/ngc-scalingo-buildpack)).
- Initialisation de nouveaux projets structurants ([nosgestesclimat-aides](/repos/incubateur-ademe/nosgestesclimat-aides), [france-chaleur-urbaine-ifpen](/repos/incubateur-ademe/france-chaleur-urbaine-ifpen), [impactco2-integrabook](/repos/incubateur-ademe/impactco2-integrabook)).

## Dépôts les plus actifs
- [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat) : Évolutions majeures du modèle de calcul, ajout de l'IA et optimisation du CI/CD.
- [benefriches](/repos/incubateur-ademe/benefriches) : Refonte importante de l'expérience utilisateur et restructuration majeure du code.
- [plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail) : Migration complète du CMS vers Wagtail et refonte de l'infrastructure avec Terraform.
- [dsfr-override](/repos/incubateur-ademe/dsfr-override) : Transformation profonde vers une interface de personnalisation visuelle et migration vers TypeScript.
- [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions) : Mise à jour des parcours utilisateurs, migration de données et corrections de sécurité critiques.
