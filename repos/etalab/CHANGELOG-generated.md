# Synthèse d'activité : etalab (du 01/06 au 10/11)

## Résumé de l'activité
L'activité de la période est marquée par une modernisation profonde des infrastructures et une montée en maturité des outils de gestion de données. Les efforts se sont concentrés sur la fiabilisation des services de transport via des mises à jour majeures de frameworks et de standards de données ([transport-site](/repos/etalab/transport-site), [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr)), garantissant des outils plus robustes et performants pour les acteurs de la mobilité.

Parallèlement, un accent particulier a été mis sur la sécurité et la conformité réglementaire, notamment pour les services administratifs ([formulaire-qf](/repos/etalab/formulaire-qf), [data_pass](/repos/etalab/data_pass)). Ces interventions visent à renforcer la protection des données personnelles et à stabiliser les processus d'authentification, assurant ainsi une expérience utilisateur plus sûre et plus fluide.

## Sécurité
- **Protection des données et conformité (RGPD)** : Nettoyage des flux de données pour empêcher l'envoi d'informations sensibles vers les outils de suivi d'erreurs ([formulaire-qf](/repos/etalab/formulaire-qf)).
- **Renforcement des accès** : Mise en place de la double authentification (2FA) et rotation des tokens de sécurité ([data_pass](/repos/etalab/data_pass), [admin_api_entreprise](/repos/etalab/admin_api_entreprise)).
- **Sécurisation des dépendances** : Renforcement de la chaîne d'intégration continue pour bloquer l'utilisation de bibliothèques présentant des vulnérabilités ([formulaire-qf](/repos/etalab/formulaire-qf)).

## Autres changements notables
- **Modernisation technologique** : Migrations majeures vers de nouveaux frameworks et versions de langages (Phoenix 1.8/Elixir 1.20 pour [transport-site](/repos/etalab/transport-site), et mises à jour Ruby/Rails pour [formulaire-qf](/repos/etalab/formulaire-qf)).
- **Évolution des standards et schémas de données** : Introduction d'une architecture permettant l'extension des schémas via des "data packages" ([schema-dispositif-aide](/repos/etalab/schema-dispositif-aide)) et mise à jour majeure du profil France NeTEx ([transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr)).
- **Optimisation des performances et de la fiabilité** : Amélioration de la gestion de la mémoire en production ([transport-validator](/repos/etalab/transport-validator)), centralisation du traitement des données de transport ([transport-site](/repos/etalab/transport-site)) et automatisation des cycles de vie via API ([data_pass](/repos/etalab/data_pass)).
- **Intégrations et API** : Nouvelles connexions avec des partenaires institutionnels (CNOUS, MSA, MEN) ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Modernisation complète du framework, refonte du backoffice et fiabilisation du traitement des données NeTEx.
- [formulaire-qf](/repos/etalab/formulaire-qf) : Travaux intensifs sur la sécurité RGPD, la gestion des sessions FranceConnect et la mise à jour des technologies backend.
- [data_pass](/repos/etalab/data_pass) : Automatisation des processus métier via API et renforcement de la sécurité des accès.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Nouvelles intégrations API et gestion optimisée des tokens et de l'interface.
